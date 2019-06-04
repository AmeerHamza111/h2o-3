#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# This file is auto-generated by h2o-3/h2o-bindings/bin/gen_python.py
# Copyright 2016 H2O.ai;  Apache License Version 2.0 (see LICENSE for details)
#
from __future__ import absolute_import, division, print_function, unicode_literals

from h2o.estimators.estimator_base import H2OEstimator
from h2o.exceptions import H2OValueError
from h2o.frame import H2OFrame
from h2o.utils.typechecks import assert_is_type, Enum, numeric


class H2OSingularValueDecompositionEstimator(H2OEstimator):
    """
    Singular Value Decomposition

    """

    algo = "svd"

    def __init__(self, **kwargs):
        super(H2OSingularValueDecompositionEstimator, self).__init__()
        self._parms = {}
        names_list = {"model_id", "training_frame", "validation_frame", "ignored_columns", "ignore_const_cols",
                      "score_each_iteration", "transform", "svd_method", "nv", "max_iterations", "seed", "keep_u",
                      "u_name", "use_all_factor_levels", "max_runtime_secs", "export_checkpoints_dir"}
        if "Lambda" in kwargs: kwargs["lambda_"] = kwargs.pop("Lambda")
        for pname, pvalue in kwargs.items():
            if pname == 'model_id':
                self._id = pvalue
                self._parms["model_id"] = pvalue
            elif pname in names_list:
                # Using setattr(...) will invoke type-checking of the arguments
                setattr(self, pname, pvalue)
            else:
                raise H2OValueError("Unknown parameter %s = %r" % (pname, pvalue))

    @property
    def training_frame(self):
        """
        Id of the training data frame.

        Type: ``H2OFrame``.
        """
        return self._parms.get("training_frame")

    @training_frame.setter
    def training_frame(self, training_frame):
        self._parms["training_frame"] = H2OFrame._validate(training_frame, 'training_frame')


    @property
    def validation_frame(self):
        """
        Id of the validation data frame.

        Type: ``H2OFrame``.
        """
        return self._parms.get("validation_frame")

    @validation_frame.setter
    def validation_frame(self, validation_frame):
        self._parms["validation_frame"] = H2OFrame._validate(validation_frame, 'validation_frame')


    @property
    def ignored_columns(self):
        """
        Names of columns to ignore for training.

        Type: ``List[str]``.
        """
        return self._parms.get("ignored_columns")

    @ignored_columns.setter
    def ignored_columns(self, ignored_columns):
        assert_is_type(ignored_columns, None, [str])
        self._parms["ignored_columns"] = ignored_columns


    @property
    def ignore_const_cols(self):
        """
        Ignore constant columns.

        Type: ``bool``  (default: ``True``).
        """
        return self._parms.get("ignore_const_cols")

    @ignore_const_cols.setter
    def ignore_const_cols(self, ignore_const_cols):
        assert_is_type(ignore_const_cols, None, bool)
        self._parms["ignore_const_cols"] = ignore_const_cols


    @property
    def score_each_iteration(self):
        """
        Whether to score during each iteration of model training.

        Type: ``bool``  (default: ``False``).
        """
        return self._parms.get("score_each_iteration")

    @score_each_iteration.setter
    def score_each_iteration(self, score_each_iteration):
        assert_is_type(score_each_iteration, None, bool)
        self._parms["score_each_iteration"] = score_each_iteration


    @property
    def transform(self):
        """
        Transformation of training data

        One of: ``"none"``, ``"standardize"``, ``"normalize"``, ``"demean"``, ``"descale"``  (default: ``"none"``).
        """
        return self._parms.get("transform")

    @transform.setter
    def transform(self, transform):
        assert_is_type(transform, None, Enum("none", "standardize", "normalize", "demean", "descale"))
        self._parms["transform"] = transform


    @property
    def svd_method(self):
        """
        Method for computing SVD (Caution: Randomized is currently experimental and unstable)

        One of: ``"gram_s_v_d"``, ``"power"``, ``"randomized"``  (default: ``"gram_s_v_d"``).
        """
        return self._parms.get("svd_method")

    @svd_method.setter
    def svd_method(self, svd_method):
        assert_is_type(svd_method, None, Enum("gram_s_v_d", "power", "randomized"))
        self._parms["svd_method"] = svd_method


    @property
    def nv(self):
        """
        Number of right singular vectors

        Type: ``int``  (default: ``1``).
        """
        return self._parms.get("nv")

    @nv.setter
    def nv(self, nv):
        assert_is_type(nv, None, int)
        self._parms["nv"] = nv


    @property
    def max_iterations(self):
        """
        Maximum iterations

        Type: ``int``  (default: ``1000``).
        """
        return self._parms.get("max_iterations")

    @max_iterations.setter
    def max_iterations(self, max_iterations):
        assert_is_type(max_iterations, None, int)
        self._parms["max_iterations"] = max_iterations


    @property
    def seed(self):
        """
        RNG seed for k-means++ initialization

        Type: ``int``  (default: ``-1``).
        """
        return self._parms.get("seed")

    @seed.setter
    def seed(self, seed):
        assert_is_type(seed, None, int)
        self._parms["seed"] = seed


    @property
    def keep_u(self):
        """
        Save left singular vectors?

        Type: ``bool``  (default: ``True``).
        """
        return self._parms.get("keep_u")

    @keep_u.setter
    def keep_u(self, keep_u):
        assert_is_type(keep_u, None, bool)
        self._parms["keep_u"] = keep_u


    @property
    def u_name(self):
        """
        Frame key to save left singular vectors

        Type: ``str``.
        """
        return self._parms.get("u_name")

    @u_name.setter
    def u_name(self, u_name):
        assert_is_type(u_name, None, str)
        self._parms["u_name"] = u_name


    @property
    def use_all_factor_levels(self):
        """
        Whether first factor level is included in each categorical expansion

        Type: ``bool``  (default: ``True``).
        """
        return self._parms.get("use_all_factor_levels")

    @use_all_factor_levels.setter
    def use_all_factor_levels(self, use_all_factor_levels):
        assert_is_type(use_all_factor_levels, None, bool)
        self._parms["use_all_factor_levels"] = use_all_factor_levels


    @property
    def max_runtime_secs(self):
        """
        Maximum allowed runtime in seconds for model training. Use 0 to disable.

        Type: ``float``  (default: ``0``).
        """
        return self._parms.get("max_runtime_secs")

    @max_runtime_secs.setter
    def max_runtime_secs(self, max_runtime_secs):
        assert_is_type(max_runtime_secs, None, numeric)
        self._parms["max_runtime_secs"] = max_runtime_secs


    @property
    def export_checkpoints_dir(self):
        """
        Automatically export generated models to this directory.

        Type: ``str``.
        """
        return self._parms.get("export_checkpoints_dir")

    @export_checkpoints_dir.setter
    def export_checkpoints_dir(self, export_checkpoints_dir):
        assert_is_type(export_checkpoints_dir, None, str)
        self._parms["export_checkpoints_dir"] = export_checkpoints_dir


