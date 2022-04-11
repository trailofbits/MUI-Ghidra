package mui;

import java.awt.*;
import java.awt.event.*;
import javax.swing.Box;
import javax.swing.JButton;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JToggleButton;
import javax.swing.JToolBar;
import javax.swing.ScrollPaneConstants;
import resources.ResourceManager;

/**
 * Provides the component for the Tab Content in the MUI Log tabbed pane.
 */
public class MUILogContentComponent extends JPanel {

	public ManticoreRunner manticoreRunner;

	public JTextArea logArea;
	public JButton stopButton;
	public JToggleButton scrollLockButton;

	public MUILogContentComponent(ManticoreRunner mcore) {

		manticoreRunner = mcore;

		setLayout(new BorderLayout());
		setMinimumSize(new Dimension(300, 300));

		logArea = new JTextArea();
		stopButton = new JButton();
		scrollLockButton = new JToggleButton();

		buildLogArea();
		buildToolBar();
	}

	/**
	 * Builds a scrollable, uneditable TextArea which displays the logs of a Manticore instance.
	 */
	public void buildLogArea() {
		logArea.setEditable(false);
		logArea.setLineWrap(true);
		logArea.setWrapStyleWord(true);
		JScrollPane logScrollPane =
			new JScrollPane(
				logArea,
				ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED,
				ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED);

		add(logScrollPane, BorderLayout.CENTER);
	}

	/**
	 * Builds the log's toolbar including a Stop button that will terminate the Manticore instance of the currently-focused tab.
	 */
	public void buildToolBar() {
		JToolBar logToolBar = new JToolBar();
		logToolBar.setFloatable(false);
		stopButton.setEnabled(true);
		stopButton.setIcon(ResourceManager.loadImage("images/stopNode.png"));
		stopButton.addActionListener(
			new ActionListener() {

				@Override
				public void actionPerformed(ActionEvent e) {
					manticoreRunner.terminateManticore();
				}

			});
		stopButton.setToolTipText("Terminate Execution");

		scrollLockButton.setEnabled(true);
		scrollLockButton.setIcon(ResourceManager.loadImage("images/lock.png"));
		scrollLockButton.setToolTipText("Toggle Auto-Scroll Lock");

		logToolBar.add(Box.createGlue()); // shifts buttons to the right
		logToolBar.add(stopButton);
		logToolBar.add(scrollLockButton);

		add(logToolBar, BorderLayout.PAGE_START);
	}
}
