"""占位测试 - 项目初始化验证"""
import pytest


def test_project_initialized():
    """验证项目已正确初始化"""
    assert True


def test_python_version():
    """验证 Python 版本"""
    import sys
    assert sys.version_info >= (3, 12)
