package mui;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import javax.swing.JButton;
import javax.swing.JTextArea;
import javax.swing.SwingWorker;
import javax.swing.tree.TreePath;

import ghidra.util.Msg;
import muicore.MUICore;

import java.io.*;
import java.net.*;
import java.time.Instant;
import java.util.HashSet;
import java.util.List;

/**
 * The class representing each instance of Manticore.
 */
public class ManticoreRunner {

	private Boolean isTerminated;
	private JTextArea logArea;
	private JButton stopButton;
	private MUILogContentComponent logContentComponent;

	private String host;
	private int port;

	public HashSet<TreePath> expandedPaths;
	public ManticoreStateListModel stateListModel;

	public ManticoreRunner(JTextArea logArea, JButton stopButton) {
		stateListModel = new ManticoreStateListModel();
		isTerminated = false;
		this.logArea = logArea;
		this.stopButton = stopButton;
		expandedPaths = new HashSet();

		host = "localhost";
		port = 3214;
	}

	/**
	 * Gracefully terminates the Manticore process.
	 */
	public void stopProc() {
		isTerminated = true;
	}

	/**
	 * Opens a new thread to run an instance of Manticore using the arguments specified.
	 * @param command Full Manticore command to be passed to ProcessBuilder.
	 * @param portUsed Chosen port for the Log server (+1 for State server).
	 */
	public void callProc(String[] command, int portUsed) {

		stopButton.setEnabled(true);
		logArea.append(
			"Command: " + String.join(" ", command) + System.lineSeparator() +
				System.lineSeparator());

		port = portUsed;

		SwingWorker sw =
			new SwingWorker() {
				Boolean errored = false;

				@Override
				protected Object doInBackground() throws Exception {
					ProcessBuilder pb = new ProcessBuilder(command);
					try {
						Msg.info(this, "called doInBackground");
						Process p = pb.start();
						BufferedReader reader =
							new BufferedReader(new InputStreamReader(p.getInputStream()));
						String line = "";
						long prevtime = Instant.now().getEpochSecond();

						while ((line = reader.readLine()) != null && !isTerminated) {
							logArea.append(line);
							logArea.append(System.lineSeparator());
							if (Instant.now().getEpochSecond() - 2 > prevtime) { // >1s between updates
								Msg.info(this, "attempting fetchstate");
								prevtime = Instant.now().getEpochSecond();
								try {
									Socket stateSock = new Socket(host, port + 1); // port + 1 to get state server
									InputStream stateInputStream = stateSock.getInputStream();
									try {
										List<MUICore.State> states =
											MUICore.StateList
													.parseFrom(stateInputStream.readAllBytes())
													.getStatesList();
										if (states.size() > 0) {
											ManticoreStateListModel newModel =
												new ManticoreStateListModel();
											for (MUICore.State s : states) {
												newModel.stateList.get(s.getType()).add(s);
											}
											updateStateList(newModel);
										}

									}
									catch (Exception e) {
										Msg.info(this, e.toString());
									}
									stateSock.close();
								}
								catch (IOException se) {
									Msg.info(this, se.toString());
								}
							}
						}
						if (isTerminated) {
							p.destroy();
						}
						else {
							p.waitFor();
							final int exitValue = p.waitFor();
							if (exitValue != 0) {
								errored = true;
								try (final BufferedReader b =
									new BufferedReader(new InputStreamReader(p.getErrorStream()))) {
									String eline;
									if ((eline = b.readLine()) != null) {
										logArea.append(eline);
									}
								}
								catch (final IOException e) {
									e.printStackTrace();
								}
							}
						}
						reader.close();

					}
					catch (Exception e1) {
						errored = true;
						logArea.append(e1.getMessage());
						e1.printStackTrace();
					}
					return null;
				}

				@Override
				protected void done() {
					if (isTerminated) {
						logArea.append("Manticore stopped by user.");
					}
					else if (errored) {
						logArea.append("Error! See stack trace above.");
					}
					else {
						logArea.append("Manticore execution complete.");
					}
					stopButton.setEnabled(false);
				}
			};
		sw.execute();
	}

	/**
	 * Updates the State List shown only if the Log tab of the Manticore instance is currently being viewed.
	 * @param model Updated model reflecting existing States and their statuses.
	 */
	private void updateStateList(ManticoreStateListModel model) {
		stateListModel = model;
		if (MUIStateListProvider.runnerDisplayed == this) {
			MUIStateListProvider.tryUpdate(model);
		}
	}

}
