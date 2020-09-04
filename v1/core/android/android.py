# -*- coding: utf-8 -*-
"""
    :author: ATao
    :description: 
"""

from core.android.adb import ADB
from core.device import Device
from core.android.constant import CAP_METHOD, TOUCH_METHOD, IME_METHOD, ORI_METHOD


class Android(Device):
    """Android Device Class"""

    def __init__(self, serialno=None, host=None,
                 cap_method=CAP_METHOD.MINICAP_STREAM,
                 touch_method=TOUCH_METHOD.MINITOUCH,
                 ime_method=IME_METHOD.YOSEMITEIME,
                 ori_method=ORI_METHOD.MINICAP,
                 ):
        super(Android, self).__init__()
        self.serialno = serialno or self.get_default_device()
        self.adb = ADB(self.serialno, server_addr=host)

    def get_default_device(self):
        """
        Get local default device when no serailno

        Returns:
            local device serialno

        """
        if not ADB().devices(state="device"):
            raise IndexError("ADB devices not found")
        return ADB().devices(state="device")[0][0]

    def list_app(self, third_only=False):
        """
        Return list of packages

        Args:
            third_only: if True, only third party applications are listed

        Returns:
            array of applications

        """
        return self.adb.list_app(third_only)

    def path_app(self, package):
        """
        Print the full path to the package

        Args:
            package: package name

        Returns:
            the full path to the package

        """
        return self.adb.path_app(package)

    def check_app(self, package):
        """
        Check if package exists on the device

        Args:
            package: package name

        Returns:
            AirtestError: if package is not found
            True if package exists on the device

        """
        return self.adb.check_app(package)

    def start_app(self, package, activity=None):
        """
        Start the application and activity

        Args:
            package: package name
            activity: activity name

        Returns:
            None

        """
        return self.adb.start_app(package, activity)

    def start_app_timing(self, package, activity):
        """
        Start the application and activity, and measure time

        Args:
            package: package name
            activity: activity name

        Returns:
            app launch time

        """
        return self.adb.start_app_timing(package, activity)

    def stop_app(self, package):
        """
        Stop the application

        Args:
            package: package name

        Returns:
            None

        """
        return self.adb.stop_app(package)

    def clear_app(self, package):
        """
        Clear all application data

        Args:
            package: package name

        Returns:
            None

        """
        return self.adb.clear_app(package)

    def install_app(self, filepath, replace=False, install_options=None):
        """
        Install the application on the device

        Args:
            filepath: full path to the `apk` file to be installed on the device
            replace: True or False to replace the existing application
            install_options: list of options, default is []

        Returns:
            output from installation process

        """
        return self.adb.install_app(filepath, replace=replace, install_options=install_options)

    def uninstall_app(self, package):
        """
        uninstall package

        Args:
            package: package name

        Returns:
            None

        """
        return self.adb.uninstall_app(package)