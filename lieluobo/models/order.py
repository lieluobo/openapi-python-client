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

class Order(object):
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
        'job_id': 'str',
        'resume_id': 'str',
        'order_no': 'str',
        'status': 'int',
        'url': 'str'
    }

    attribute_map = {
        'job_id': 'jobId',
        'resume_id': 'resumeId',
        'order_no': 'orderNo',
        'status': 'status',
        'url': 'url'
    }

    def __init__(self, job_id=None, resume_id=None, order_no=None, status=None, url=None):  # noqa: E501
        """Order - a model defined in Swagger"""  # noqa: E501
        self._job_id = None
        self._resume_id = None
        self._order_no = None
        self._status = None
        self._url = None
        self.discriminator = None
        if job_id is not None:
            self.job_id = job_id
        if resume_id is not None:
            self.resume_id = resume_id
        if order_no is not None:
            self.order_no = order_no
        if status is not None:
            self.status = status
        if url is not None:
            self.url = url

    @property
    def job_id(self):
        """Gets the job_id of this Order.  # noqa: E501

        职位ID  # noqa: E501

        :return: The job_id of this Order.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this Order.

        职位ID  # noqa: E501

        :param job_id: The job_id of this Order.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def resume_id(self):
        """Gets the resume_id of this Order.  # noqa: E501

        简历ID  # noqa: E501

        :return: The resume_id of this Order.  # noqa: E501
        :rtype: str
        """
        return self._resume_id

    @resume_id.setter
    def resume_id(self, resume_id):
        """Sets the resume_id of this Order.

        简历ID  # noqa: E501

        :param resume_id: The resume_id of this Order.  # noqa: E501
        :type: str
        """

        self._resume_id = resume_id

    @property
    def order_no(self):
        """Gets the order_no of this Order.  # noqa: E501

        订单号  # noqa: E501

        :return: The order_no of this Order.  # noqa: E501
        :rtype: str
        """
        return self._order_no

    @order_no.setter
    def order_no(self, order_no):
        """Sets the order_no of this Order.

        订单号  # noqa: E501

        :param order_no: The order_no of this Order.  # noqa: E501
        :type: str
        """

        self._order_no = order_no

    @property
    def status(self):
        """Gets the status of this Order.  # noqa: E501

        订单状态  # noqa: E501

        :return: The status of this Order.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Order.

        订单状态  # noqa: E501

        :param status: The status of this Order.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def url(self):
        """Gets the url of this Order.  # noqa: E501

        订单地址  # noqa: E501

        :return: The url of this Order.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Order.

        订单地址  # noqa: E501

        :param url: The url of this Order.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(Order, dict):
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
        if not isinstance(other, Order):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
