# -*- coding: utf-8 -*-

__all__ = [
            "AndroidDevDiagMonitor",
            "AndroidQmdlMonitor",
            "Monitor",
            "DMCollector",  ### P4A: THIS LINE WILL BE DELETED ###
            "Replayer",
            "OfflineReplayer"
            ]

is_android=False
try:
    from jnius import autoclass #For Android
    is_android = True
except Exception, e:
    #not used, but bugs may exist on laptop
    is_android=False


if is_android:
    from android_dev_diag_monitor import AndroidDevDiagMonitor
    from android_qmdl_monitor import AndroidQmdlMonitor
from monitor import Monitor
from dm_collector import * ### P4A: THIS LINE WILL BE DELETED ###
from replayer import Replayer
from offline_replayer import OfflineReplayer
