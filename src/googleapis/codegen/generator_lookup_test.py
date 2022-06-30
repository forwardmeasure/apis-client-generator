#!/usr/bin/python3
# Copyright 2012 Google Inc. All Rights Reserved.

"""Tests for generator_lookup."""

__author__ = 'akesling@google.com (Alex Kesling)'

import json
import os


from absl.testing import absltest

import generator_lookup
import gwt_generator
import java_generator
import targets


class GeneratorLookupTest(absltest.TestCase):

    def testDetermineGenerator(self):
        test_gen = generator_lookup.GetGeneratorByLanguage('java')
        self.assertEqual(java_generator.Java14Generator, test_gen)
        self.assertRaises(
            ValueError, generator_lookup.GetGeneratorByLanguage,
            'I\'m an invalid language!')

    def testSupportedLanguage(self):
        languages = generator_lookup.SupportedLanguages()
        self.assertContainsSubset(['dart', 'gwt', 'java', 'php'], languages)
        self.assertNotIn('java-head', languages)

    def testVersionFromFeature(self):
        template_root = os.path.join(os.path.dirname(__file__),
                                     'testdata/languages')
        targets.Targets.SetDefaultTemplateRoot(template_root)
        features_path = os.path.join(template_root,
                                     'java/generator_test/features.json')
        raw_features = json.load(open(features_path))
        generator_name = raw_features['generator']
        gen = generator_lookup.GetGeneratorByLanguage(generator_name)
        self.assertEquals(gwt_generator.GwtGenerator, gen)


if __name__ == '__main__':
    basetest.main()
