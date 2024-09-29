# Fuzzing for Type Hinting in Python

We implement and analyze three fuzzers:

- [SimpleFuzzer.py](SimpleFuzzer.py) - A simple, not-very-intelligent fuzzer. It randomly tries different combinations of types, records the ones that work, and returns those.A
- [IntellegentBlackBoxFuzzer.py](IntelligentBlackBoxFuzzer.py) - A much more intelligent version of the SimpleFuzzer - it tries to fuzz types based on the TypeError message content.
- [WhiteBoxFuzzer.py](WhiteBoxFuzzer.py) - A whitebox fuzzer that uses a function's AST to generate type constraints.

All fuzzers extend [FuzzerBase.py](FuzzerBase.py), which holds instrumentation data. An example for how to plot this data is shown in metrics_example.py


See the presentation poster [here](Presentation_Poster.pdf).
