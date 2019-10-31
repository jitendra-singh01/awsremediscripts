# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .image_template_customizer_py3 import ImageTemplateCustomizer


class ImageTemplateFileCustomizer(ImageTemplateCustomizer):
    """Uploads files to VMs (Linux, Windows). Corresponds to Packer file
    provisioner.

    All required parameters must be populated in order to send to Azure.

    :param name: Friendly Name to provide context on what this customization
     step does
    :type name: str
    :param type: Required. Constant filled by server.
    :type type: str
    :param source_uri: The URI of the file to be uploaded for customizing the
     VM. It can be a github link, SAS URI for Azure Storage, etc
    :type source_uri: str
    :param destination: The absolute path to a file (with nested directory
     structures already created) where the file (from sourceUri) will be
     uploaded to in the VM
    :type destination: str
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'source_uri': {'key': 'sourceUri', 'type': 'str'},
        'destination': {'key': 'destination', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, source_uri: str=None, destination: str=None, **kwargs) -> None:
        super(ImageTemplateFileCustomizer, self).__init__(name=name, **kwargs)
        self.source_uri = source_uri
        self.destination = destination
        self.type = 'File'
