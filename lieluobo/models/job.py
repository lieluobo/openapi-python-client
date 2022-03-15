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

class Job(object):
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
        'id': 'str',
        'title': 'str',
        'title_extend': 'str',
        'salary': 'AllOfJobSalary',
        'address': 'str',
        'required_degree': 'str',
        'headcount': 'int',
        'grade': 'AllOfJobGrade',
        'fast_pay': 'bool',
        'brokerage': 'float',
        'warranty': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'title_extend': 'titleExtend',
        'salary': 'salary',
        'address': 'address',
        'required_degree': 'requiredDegree',
        'headcount': 'headcount',
        'grade': 'grade',
        'fast_pay': 'fastPay',
        'brokerage': 'brokerage',
        'warranty': 'warranty',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'url': 'url'
    }

    def __init__(self, id=None, title=None, title_extend=None, salary=None, address=None, required_degree=None, headcount=None, grade=None, fast_pay=None, brokerage=None, warranty=None, created_at=None, updated_at=None, url=None):  # noqa: E501
        """Job - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._title = None
        self._title_extend = None
        self._salary = None
        self._address = None
        self._required_degree = None
        self._headcount = None
        self._grade = None
        self._fast_pay = None
        self._brokerage = None
        self._warranty = None
        self._created_at = None
        self._updated_at = None
        self._url = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if title_extend is not None:
            self.title_extend = title_extend
        if salary is not None:
            self.salary = salary
        if address is not None:
            self.address = address
        if required_degree is not None:
            self.required_degree = required_degree
        if headcount is not None:
            self.headcount = headcount
        if grade is not None:
            self.grade = grade
        if fast_pay is not None:
            self.fast_pay = fast_pay
        if brokerage is not None:
            self.brokerage = brokerage
        if warranty is not None:
            self.warranty = warranty
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if url is not None:
            self.url = url

    @property
    def id(self):
        """Gets the id of this Job.  # noqa: E501


        :return: The id of this Job.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Job.


        :param id: The id of this Job.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this Job.  # noqa: E501


        :return: The title of this Job.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Job.


        :param title: The title of this Job.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def title_extend(self):
        """Gets the title_extend of this Job.  # noqa: E501


        :return: The title_extend of this Job.  # noqa: E501
        :rtype: str
        """
        return self._title_extend

    @title_extend.setter
    def title_extend(self, title_extend):
        """Sets the title_extend of this Job.


        :param title_extend: The title_extend of this Job.  # noqa: E501
        :type: str
        """

        self._title_extend = title_extend

    @property
    def salary(self):
        """Gets the salary of this Job.  # noqa: E501


        :return: The salary of this Job.  # noqa: E501
        :rtype: AllOfJobSalary
        """
        return self._salary

    @salary.setter
    def salary(self, salary):
        """Sets the salary of this Job.


        :param salary: The salary of this Job.  # noqa: E501
        :type: AllOfJobSalary
        """

        self._salary = salary

    @property
    def address(self):
        """Gets the address of this Job.  # noqa: E501


        :return: The address of this Job.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Job.


        :param address: The address of this Job.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def required_degree(self):
        """Gets the required_degree of this Job.  # noqa: E501


        :return: The required_degree of this Job.  # noqa: E501
        :rtype: str
        """
        return self._required_degree

    @required_degree.setter
    def required_degree(self, required_degree):
        """Sets the required_degree of this Job.


        :param required_degree: The required_degree of this Job.  # noqa: E501
        :type: str
        """

        self._required_degree = required_degree

    @property
    def headcount(self):
        """Gets the headcount of this Job.  # noqa: E501


        :return: The headcount of this Job.  # noqa: E501
        :rtype: int
        """
        return self._headcount

    @headcount.setter
    def headcount(self, headcount):
        """Sets the headcount of this Job.


        :param headcount: The headcount of this Job.  # noqa: E501
        :type: int
        """

        self._headcount = headcount

    @property
    def grade(self):
        """Gets the grade of this Job.  # noqa: E501


        :return: The grade of this Job.  # noqa: E501
        :rtype: AllOfJobGrade
        """
        return self._grade

    @grade.setter
    def grade(self, grade):
        """Sets the grade of this Job.


        :param grade: The grade of this Job.  # noqa: E501
        :type: AllOfJobGrade
        """

        self._grade = grade

    @property
    def fast_pay(self):
        """Gets the fast_pay of this Job.  # noqa: E501


        :return: The fast_pay of this Job.  # noqa: E501
        :rtype: bool
        """
        return self._fast_pay

    @fast_pay.setter
    def fast_pay(self, fast_pay):
        """Sets the fast_pay of this Job.


        :param fast_pay: The fast_pay of this Job.  # noqa: E501
        :type: bool
        """

        self._fast_pay = fast_pay

    @property
    def brokerage(self):
        """Gets the brokerage of this Job.  # noqa: E501


        :return: The brokerage of this Job.  # noqa: E501
        :rtype: float
        """
        return self._brokerage

    @brokerage.setter
    def brokerage(self, brokerage):
        """Sets the brokerage of this Job.


        :param brokerage: The brokerage of this Job.  # noqa: E501
        :type: float
        """

        self._brokerage = brokerage

    @property
    def warranty(self):
        """Gets the warranty of this Job.  # noqa: E501


        :return: The warranty of this Job.  # noqa: E501
        :rtype: str
        """
        return self._warranty

    @warranty.setter
    def warranty(self, warranty):
        """Sets the warranty of this Job.


        :param warranty: The warranty of this Job.  # noqa: E501
        :type: str
        """

        self._warranty = warranty

    @property
    def created_at(self):
        """Gets the created_at of this Job.  # noqa: E501


        :return: The created_at of this Job.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Job.


        :param created_at: The created_at of this Job.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Job.  # noqa: E501


        :return: The updated_at of this Job.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Job.


        :param updated_at: The updated_at of this Job.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def url(self):
        """Gets the url of this Job.  # noqa: E501


        :return: The url of this Job.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Job.


        :param url: The url of this Job.  # noqa: E501
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
        if issubclass(Job, dict):
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
        if not isinstance(other, Job):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
