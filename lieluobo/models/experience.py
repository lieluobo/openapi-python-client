# coding: utf-8

"""
    猎萝卜开放平台

    猎萝卜开放平台  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Experience(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'org_name': 'str',
        'dept_name': 'str',
        'started_at': 'date',
        'ended_at': 'date',
        'position': 'str',
        'description': 'str',
        'level': 'str',
        'in_service': 'bool'
    }

    attribute_map = {
        'org_name': 'orgName',
        'dept_name': 'deptName',
        'started_at': 'startedAt',
        'ended_at': 'endedAt',
        'position': 'position',
        'description': 'description',
        'level': 'level',
        'in_service': 'inService'
    }

    def __init__(self, org_name=None, dept_name=None, started_at=None, ended_at=None, position=None, description=None, level=None, in_service=None):  # noqa: E501
        """Experience - a model defined in Swagger"""  # noqa: E501
        self._org_name = None
        self._dept_name = None
        self._started_at = None
        self._ended_at = None
        self._position = None
        self._description = None
        self._level = None
        self._in_service = None
        self.discriminator = None
        self.org_name = org_name
        if dept_name is not None:
            self.dept_name = dept_name
        self.started_at = started_at
        if ended_at is not None:
            self.ended_at = ended_at
        self.position = position
        self.description = description
        if level is not None:
            self.level = level
        if in_service is not None:
            self.in_service = in_service

    @property
    def org_name(self):
        """Gets the org_name of this Experience.  # noqa: E501


        :return: The org_name of this Experience.  # noqa: E501
        :rtype: str
        """
        return self._org_name

    @org_name.setter
    def org_name(self, org_name):
        """Sets the org_name of this Experience.


        :param org_name: The org_name of this Experience.  # noqa: E501
        :type: str
        """
        if org_name is None:
            raise ValueError("Invalid value for `org_name`, must not be `None`")  # noqa: E501

        self._org_name = org_name

    @property
    def dept_name(self):
        """Gets the dept_name of this Experience.  # noqa: E501


        :return: The dept_name of this Experience.  # noqa: E501
        :rtype: str
        """
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        """Sets the dept_name of this Experience.


        :param dept_name: The dept_name of this Experience.  # noqa: E501
        :type: str
        """

        self._dept_name = dept_name

    @property
    def started_at(self):
        """Gets the started_at of this Experience.  # noqa: E501


        :return: The started_at of this Experience.  # noqa: E501
        :rtype: date
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this Experience.


        :param started_at: The started_at of this Experience.  # noqa: E501
        :type: date
        """
        if started_at is None:
            raise ValueError("Invalid value for `started_at`, must not be `None`")  # noqa: E501

        self._started_at = started_at

    @property
    def ended_at(self):
        """Gets the ended_at of this Experience.  # noqa: E501


        :return: The ended_at of this Experience.  # noqa: E501
        :rtype: date
        """
        return self._ended_at

    @ended_at.setter
    def ended_at(self, ended_at):
        """Sets the ended_at of this Experience.


        :param ended_at: The ended_at of this Experience.  # noqa: E501
        :type: date
        """

        self._ended_at = ended_at

    @property
    def position(self):
        """Gets the position of this Experience.  # noqa: E501


        :return: The position of this Experience.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Experience.


        :param position: The position of this Experience.  # noqa: E501
        :type: str
        """
        if position is None:
            raise ValueError("Invalid value for `position`, must not be `None`")  # noqa: E501

        self._position = position

    @property
    def description(self):
        """Gets the description of this Experience.  # noqa: E501


        :return: The description of this Experience.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Experience.


        :param description: The description of this Experience.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def level(self):
        """Gets the level of this Experience.  # noqa: E501


        :return: The level of this Experience.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this Experience.


        :param level: The level of this Experience.  # noqa: E501
        :type: str
        """

        self._level = level

    @property
    def in_service(self):
        """Gets the in_service of this Experience.  # noqa: E501


        :return: The in_service of this Experience.  # noqa: E501
        :rtype: bool
        """
        return self._in_service

    @in_service.setter
    def in_service(self, in_service):
        """Sets the in_service of this Experience.


        :param in_service: The in_service of this Experience.  # noqa: E501
        :type: bool
        """

        self._in_service = in_service

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Experience, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Experience):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
