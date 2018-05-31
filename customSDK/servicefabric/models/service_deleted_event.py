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

from .service_event import ServiceEvent


class ServiceDeletedEvent(ServiceEvent):
    """Service Deleted event.

    :param event_instance_id: The identifier for the FabricEvent instance.
    :type event_instance_id: str
    :param time_stamp: The time event was logged.
    :type time_stamp: datetime
    :param has_correlated_events: Shows there is existing related events
     available.
    :type has_correlated_events: bool
    :param kind: Constant filled by server.
    :type kind: str
    :param service_id: The identity of the service. This is an encoded
     representation of the service name. This is used in the REST APIs to
     identify the service resource.
     Starting in version 6.0, hierarchical names are delimited with the "\\~"
     character. For example, if the service name is "fabric:/myapp/app1/svc1",
     the service identity would be "myapp~app1\\~svc1" in 6.0+ and
     "myapp/app1/svc1" in previous versions.
    :type service_id: str
    :param service_type_name: Service type name.
    :type service_type_name: str
    :param application_name: Application name.
    :type application_name: str
    :param application_type_name: Application type name.
    :type application_type_name: str
    :param service_instance: Id of Service instance.
    :type service_instance: long
    :param is_stateful: Indicates if Service is stateful.
    :type is_stateful: bool
    :param partition_count: Number of partitions.
    :type partition_count: int
    :param target_replica_set_size: Size of target replicas set.
    :type target_replica_set_size: int
    :param min_replica_set_size: Minimum size of replicas set.
    :type min_replica_set_size: int
    :param service_package_version: Version of Service package.
    :type service_package_version: str
    """

    _validation = {
        'event_instance_id': {'required': True},
        'time_stamp': {'required': True},
        'kind': {'required': True},
        'service_id': {'required': True},
        'service_type_name': {'required': True},
        'application_name': {'required': True},
        'application_type_name': {'required': True},
        'service_instance': {'required': True},
        'is_stateful': {'required': True},
        'partition_count': {'required': True},
        'target_replica_set_size': {'required': True},
        'min_replica_set_size': {'required': True},
        'service_package_version': {'required': True},
    }

    _attribute_map = {
        'event_instance_id': {'key': 'EventInstanceId', 'type': 'str'},
        'time_stamp': {'key': 'TimeStamp', 'type': 'iso-8601'},
        'has_correlated_events': {'key': 'HasCorrelatedEvents', 'type': 'bool'},
        'kind': {'key': 'Kind', 'type': 'str'},
        'service_id': {'key': 'ServiceId', 'type': 'str'},
        'service_type_name': {'key': 'ServiceTypeName', 'type': 'str'},
        'application_name': {'key': 'ApplicationName', 'type': 'str'},
        'application_type_name': {'key': 'ApplicationTypeName', 'type': 'str'},
        'service_instance': {'key': 'ServiceInstance', 'type': 'long'},
        'is_stateful': {'key': 'IsStateful', 'type': 'bool'},
        'partition_count': {'key': 'PartitionCount', 'type': 'int'},
        'target_replica_set_size': {'key': 'TargetReplicaSetSize', 'type': 'int'},
        'min_replica_set_size': {'key': 'MinReplicaSetSize', 'type': 'int'},
        'service_package_version': {'key': 'ServicePackageVersion', 'type': 'str'},
    }

    def __init__(self, event_instance_id, time_stamp, service_id, service_type_name, application_name, application_type_name, service_instance, is_stateful, partition_count, target_replica_set_size, min_replica_set_size, service_package_version, has_correlated_events=None):
        super(ServiceDeletedEvent, self).__init__(event_instance_id=event_instance_id, time_stamp=time_stamp, has_correlated_events=has_correlated_events, service_id=service_id)
        self.service_type_name = service_type_name
        self.application_name = application_name
        self.application_type_name = application_type_name
        self.service_instance = service_instance
        self.is_stateful = is_stateful
        self.partition_count = partition_count
        self.target_replica_set_size = target_replica_set_size
        self.min_replica_set_size = min_replica_set_size
        self.service_package_version = service_package_version
        self.kind = 'ServiceDeleted'
