"""
MAP Client Plugin Step
"""
import json

from PySide6 import QtGui

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.datamapstep.configuredialog import ConfigureDialog
from mapclientplugins.datamapstep.model.mappingmodel import MappingModel
from mapclientplugins.datamapstep.view.datamapwidget import DataMapWidget


class DataMapStep(WorkflowStepMountPoint):
    """
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    """

    def __init__(self, location):
        super(DataMapStep, self).__init__('Data Map', location)
        self._configured = False  # A step cannot be executed until it has been configured.
        self._category = 'Registration'
        # Add any other initialisation code here:
        self._icon = QtGui.QImage(':/datamapstep/images/registration.png')
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location'))
        # Port data:
        self._port0_inputZincModelFile = None  # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location
        self._port1_inputZincDataFile = None  # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location
        self._port2_outputZincModelFile = None  # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location
        # Config:
        self._config = {}
        self._config['identifier'] = ''
        self._model = None
        self._view = None

    def execute(self):
        """
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        """
        # Put your execute step code here before calling the '_doneExecution' method.
        self._model = MappingModel(self._port0_inputZincModelFile, self._port1_inputZincDataFile, self._location)
        self._view = DataMapWidget(self._model)
        self._setCurrentWidget(self._view)
        self._view.register_done_execution(self._myDoneExecution)

    def _myDoneExecution(self):
        self._port2_outputZincModelFile = None
        self._model = None
        self._view = None
        self._doneExecution()

    def setPortData(self, index, dataIn):
        """
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.

        :param index: Index of the port to return.
        :param dataIn: The data to set for the port at the given index.
        """
        if index == 0:
            self._port0_inputZincModelFile = dataIn  # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location
        elif index == 1:
            self._port1_inputZincDataFile = dataIn  # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location

    def getPortData(self, index):
        """
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.

        :param index: Index of the port to return.
        """
        # self._port2_outputZincModelFile = self._model.getOutputModelFileName()
        return self._model_port2_outputZincModelFile  # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location

    def configure(self):
        """
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        """
        dlg = ConfigureDialog(self._main_window)
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)

        if dlg.exec_():
            self._config = dlg.getConfig()

        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        """
        The identifier is a string that must be unique within a workflow.
        """
        return self._config['identifier']

    def setIdentifier(self, identifier):
        """
        The framework will set the identifier for this step when it is loaded.
        """
        self._config['identifier'] = identifier

    def serialize(self):
        """
        Add code to serialize this step to string.  This method should
        implement the opposite of 'deserialize'.
        """
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        """
        Add code to deserialize this step from string.  This method should
        implement the opposite of 'serialize'.

        :param string: JSON representation of the configuration in a string.
        """
        self._config.update(json.loads(string))

        d = ConfigureDialog()
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()
