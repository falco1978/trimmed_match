load("@rules_cc//cc:defs.bzl", "cc_library", "cc_test")
package(default_visibility = [
    "//visibility:public",
])

licenses(["notice"])

cc_library(
    name = "estimator",
    srcs = ["estimator.cc"],
    hdrs = ["estimator.h"],
    deps = [
        ":geox_data_util",
        ":math_util",
        "@abseil-cpp//absl/types:optional",
        "@glog",
    ],
)

cc_library(
    name = "geox_data_util",
    srcs = ["geox_data_util.cc"],
    hdrs = ["geox_data_util.h"],
    deps = [
        ":math_util",
        "@glog",
    ],
)

cc_library(
    name = "math_util",
    srcs = ["math_util.cc"],
    hdrs = ["math_util.h"],
    deps = ["@glog"],
)

cc_test(
    name = "estimator_test",
    srcs = ["estimator_test.cc"],
    # copts = select({
    # "@bazel_tools//tools/cpp:windows": [],
    # "//conditions:default": ["-Wno-sign-compare"],
    # }),
    deps = [
        ":estimator",
        "@googletest//:gtest_main",
    ],
)

cc_test(
    name = "geox_data_util_test",
    srcs = ["geox_data_util_test.cc"],
    # copts = select({
    # "@bazel_tools//tools/cpp:windows": [],
    # "//conditions:default": ["-Wno-sign-compare"],
    # }),
    deps = [
        ":geox_data_util",
        "@googletest//:gtest_main",
    ],
)

cc_test(
    name = "math_util_test",
    srcs = ["math_util_test.cc"],
    # copts = select({
    # "@bazel_tools//tools/cpp:windows": [],
    # "//conditions:default": ["-Wno-sign-compare"],
    # }),
    deps = [
        ":math_util",
        "@googletest//:gtest_main",
    ],
)
