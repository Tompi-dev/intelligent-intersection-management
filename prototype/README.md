# Prototype materials

Open the three SVG mockups in a browser to inspect configuration, monitoring and comparison scenarios. They are editable vector assets, not a running web application. Values are demonstration data or labelled as awaiting results.

The runnable controller uses precomputed queues, Python 3.10+ and no external dependency. From the repository root:

```sh
python3 -m src.controller --input prototype/sample_observations.json
python3 -m src.controller --input prototype/sample_observations.json --config config/timing.example.json
python3 -m unittest discover -s tests -v
```

Compare the sample output with expected_output.json. Output group refers to the current signal group while stage determines whether it is green or yellow. During ALL_RED the group is null. Calls never skip clearance stages, even when input time jumps. A continuously applied signal system would require a regular tick and an adapter with its own watchdog.

Missing or stale state selects fixed-time fallback. Malformed, future or decreasing timestamps reject the CLI input with a clear nonzero exit. The program validates all rows before printing its result, so it does not send partial control commands. Video processing and traffic simulation are planned work.
