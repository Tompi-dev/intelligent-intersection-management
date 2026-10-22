# Prototype materials

The interactive implementation now lives in `web/` and `src/web_demo.py`. Start `./run_demo.command` from the repository root and open http://127.0.0.1:8766/. It uses the actual Python controller with editable synthetic inputs, playback, configuration, feed failure scenarios and JSON evidence export. SVG/PNG files in this directory remain static mockups, separate from the interactive application.

## Interface design v0.2

Three coordinated warm-neutral research dashboards are supplied as editable SVG and PNG: configuration with run manifest, monitoring with an illustrative junction and decision inspector, and evaluation design with an explicitly schematic chart. The sidebar links navigate between the SVG screens when served locally. Form fields, charts and junction shapes are design elements; no live data binding is implemented. Monitor values correspond to the sample fixture at t=10 s, while vehicle placement is illustrative. Comparison curves are not measured results. Word and PowerPoint snapshots are not automatically regenerated when these assets change.

Open the three SVG mockups in a browser to inspect configuration, monitoring and comparison scenarios. They are editable vector assets, not a running web application. Values are demonstration data or labelled as awaiting results.

The runnable controller uses precomputed queues, Python 3.10+ and no external dependency. From the repository root:

```sh
python3 -m src.controller --input prototype/sample_observations.json
python3 -m src.controller --input prototype/sample_observations.json --config config/timing.example.json
python3 -m unittest discover -s tests -v
```

Compare the sample output with expected_output.json. Output group refers to the current signal group while stage determines whether it is green or yellow. During ALL_RED the group is null. Calls never skip clearance stages, even when input time jumps. A continuously applied signal system would require a regular tick and an adapter with its own watchdog.

Missing or stale state selects fixed-time fallback. Malformed, future or decreasing timestamps reject the CLI input with a clear nonzero exit. The program validates all rows before printing its result, so it does not send partial control commands. Video processing and traffic simulation are planned work.
