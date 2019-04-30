# -*- coding: utf-8 -*-
#
# This file is part of the DumbMaster project
#
#
#
# Distributed under the terms of the GPL license.
# See LICENSE.txt for more info.

""" DUM CSP.LMC subelement Master Tango device prototype

DumbMaster TANGO device class to test connection with the CSPMaster prototype
"""

# Tango imports
import tango
from tango import DebugIt
from tango.server import run
from tango.server import Device, DeviceMeta
from tango.server import attribute, command
from tango.server import device_property
from tango import AttrQuality, DispLevel, DevState
from tango import AttrWriteType, PipeWriteType
from skabase.SKAMaster.SKAMaster import SKAMaster
# Additional import
# PROTECTED REGION ID(DumbMaster.additionnal_import) ENABLED START #
from future.utils import with_metaclass
import time
import threading
#from csplmc.CspMaster.global_enum import HealthState, AdminMode
# PROTECTED REGION END #    //  DumbMaster.additionnal_import

__all__ = ["DumbMaster", "main"]


class DumbMaster(with_metaclass(DeviceMeta,SKAMaster)):
    """
    DumbMaster TANGO device class to test connection with the CSPMaster prototype
    """
    # PROTECTED REGION ID(DumbMaster.class_variable) ENABLED START #
    # PROTECTED REGION END #    //  DumbMaster.class_variable

    # -----------------
    # Device Properties
    # -----------------

    # ----------
    # Attributes
    # ----------

    commandProgress = attribute(
        dtype='uint16',
        label="Command progress percentage",
        max_value=100,
        min_value=0,
        polling_period=1000,
        abs_change=5,
        rel_change=2,
        doc="Percentage progress implemented for commands that  result in state/mode transitions for a large \nnumber of components and/or are executed in stages (e.g power up, power down)",
    )


    # ---------------
    # General methods
    # ---------------

    def init_subelement(self):
        """
        Simulate the sub-element device initialization
        """
        time.sleep(5)
        self.set_state(tango.DevState.STANDBY)

    def on_subelement(self):
        """
        Simulate the sub-element transition from STANDBY to ON 
        """
        time.sleep(10)
        self.set_state(tango.DevState.ON)
        #self._health_state = HealthState.DEGRADED.value
        self._health_state = 1

    def standby_subelement(self):
        """
        Simulate the sub-element transition from ON to STANDBY
        """
        time.sleep(5)
        self.set_state(tango.DevState.STANDBY)
        #self._health_state = HealthState.DEGRADED.value
        self._health_state = 1

    def init_device(self):
        SKAMaster.init_device(self)
        # PROTECTED REGION ID(DumbMaster.init_device) ENABLED START #
        self.set_state(tango.DevState.INIT)
        self._health_state = 3  
        # start a timer to simulate device intialization
        thread = threading.Timer(5, self.init_subelement)
        thread.start()

        # PROTECTED REGION END #    //  DumbMaster.init_device

    def always_executed_hook(self):
        # PROTECTED REGION ID(DumbMaster.always_executed_hook) ENABLED START #
        pass
        # PROTECTED REGION END #    //  DumbMaster.always_executed_hook

    def delete_device(self):
        # PROTECTED REGION ID(DumbMaster.delete_device) ENABLED START #
        pass
        # PROTECTED REGION END #    //  DumbMaster.delete_device

    # ------------------
    # Attributes methods
    # ------------------

    def read_commandProgress(self):
        # PROTECTED REGION ID(DumbMaster.commandProgress_read) ENABLED START #
        return 0
        # PROTECTED REGION END #    //  DumbMaster.commandProgress_read


    # --------
    # Commands
    # --------

    @command(
    dtype_in=('str',), 
    doc_in="If the array length is0, the command apllies to the whole\nCSP Element.\nIf the array length is > 1, each array element specifies the FQDN of the\nCSP SubElement to switch ON.", 
    )
    @DebugIt()
    def On(self, argin):
        # PROTECTED REGION ID(DumbMaster.On) ENABLED START #
        thread = threading.Timer(10, self.on_subelement)
        thread.start()
        # PROTECTED REGION END #    //  DumbMaster.On

    @command(
    dtype_in=('str',), 
    doc_in="If the array length is0, the command apllies to the whole\nCSP Element.\nIf the array length is > 1, each array element specifies the FQDN of the\nCSP SubElement to switch OFF.", 
    )
    @DebugIt()
    def Off(self, argin):
        # PROTECTED REGION ID(DumbMaster.Off) ENABLED START #
        pass
        # PROTECTED REGION END #    //  DumbMaster.Off

    @command(
    )
    @DebugIt()
    def Standby(self):
        # PROTECTED REGION ID(DumbMaster.Standby) ENABLED START #
        pass
        # PROTECTED REGION END #    //  DumbMaster.Standby

# ----------
# Run server
# ----------


def main(args=None, **kwargs):
    # PROTECTED REGION ID(DumbMaster.main) ENABLED START #
    return run((DumbMaster,), args=args, **kwargs)
    # PROTECTED REGION END #    //  DumbMaster.main

if __name__ == '__main__':
    main()
