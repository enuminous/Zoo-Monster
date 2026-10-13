# MONSTER — Nuisance and Out-of-control Growth Stress Test

<!-- ENUMINOUS-NETWORK:START -->
**eNuminous network:** [All repositories](https://enuminous.github.io/EFMW/repositories.html) · [EFMW](https://enuminous.github.io/EFMW/) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [165 triplets](https://enuminous.github.io/FieldSpace/) · [Zoo](https://enuminous.github.io/Tortoise/) · [Lean](https://enuminous.github.io/Aristotle-102-Monolithic-Lean/) · [Engine](https://enuminous.github.io/Archimedes-Engine/) · [Papers](https://enuminous.github.io/medium/papers-essays-index.html) · [Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/INTERLOCK_AUDIT.md)

[Repository](https://github.com/enuminous/Zoo-Monster) · This repository is linked through its source; GitHub Pages is not enabled.

<details>
<summary>Recent repositories (9)</summary>

- [Oroboros](https://github.com/enuminous/Oroboros) · [README](https://github.com/enuminous/Oroboros/blob/main/README.md) · [Page](https://enuminous.github.io/Oroboros/)
- [P-NP](https://github.com/enuminous/P-NP) · [README](https://github.com/enuminous/P-NP/blob/main/README.md) · [Page](https://enuminous.github.io/P-NP/)
- [Research-Program](https://github.com/enuminous/Research-Program) · [README](https://github.com/enuminous/Research-Program/blob/main/README.md) · [Page](https://enuminous.github.io/Research-Program/)
- [I-Have-Guts](https://github.com/enuminous/I-Have-Guts) · [README](https://github.com/enuminous/I-Have-Guts/blob/main/README.md) · [Page](https://enuminous.github.io/I-Have-Guts/)
- [Wrights-Law](https://github.com/enuminous/Wrights-Law) · [README](https://github.com/enuminous/Wrights-Law/blob/main/README.md) · [Page](https://enuminous.github.io/Wrights-Law/)
- [Aristotle-eNuminous](https://github.com/enuminous/Aristotle-eNuminous) · [README](https://github.com/enuminous/Aristotle-eNuminous/blob/main/README.md) · [Page](https://enuminous.github.io/Aristotle-eNuminous/)
- [Multiverse-Simulator](https://github.com/enuminous/Multiverse-Simulator) · [README](https://github.com/enuminous/Multiverse-Simulator/blob/main/README.md) · [Page](https://enuminous.github.io/Multiverse-Simulator/)
- [accelerando-8192](https://github.com/enuminous/accelerando-8192) · [README](https://github.com/enuminous/accelerando-8192/blob/main/README.md) · [Page source](https://github.com/enuminous/accelerando-8192/blob/main/docs/index.html)
- [Codex-888](https://github.com/enuminous/Codex-888) · [README](https://github.com/enuminous/Codex-888/blob/main/README.md) · [Page](https://enuminous.github.io/Codex-888/)

</details>
<!-- ENUMINOUS-NETWORK:END -->

**Zoo animal specification · version 1.0.0**

MONSTER tests whether a result survives plausible nuisance changes and adversarial counterexamples. It requires perturbation families and severity levels to be preregistered, compares against matched conventional baselines, reports the full performance envelope, and identifies the first failure boundary.

MONSTER answers: **Does the result remain within declared tolerances when reasonable hostile conditions change?** It does not audit how evidence was constructed; that is CIRCUS’s job.

## Fixed operation

| Field | Definition |
|---|---|
| Purpose | Measure robustness and identify where a result degrades or fails under specified nuisance shifts and counterexamples. |
| Inputs | Frozen claim, outcome metric, tolerances, perturbation families/severity, test cases, nulls, seeds, and matched baseline protocol. |
| Transformation | Execute the preregistered perturbation grid for candidate and matched baselines; preserve all outcomes; calculate envelope and first failure boundary. |
| Outputs | Preregistration record; full performance envelope; paired baseline comparisons; failure-boundary table; gate decision. |
| Pass | All predeclared tolerances are met across required perturbations, nulls, and seeds; no material unregistered exclusion or setting dependence. |
| Fail | Any required condition exceeds tolerance, a counterexample defeats the claim, or success depends on a narrow setting. |
| N/A | Required baseline, perturbation, severity, or outcome provenance is missing. N/A is not a pass. |

## Required procedure

1. **Freeze target and estimand.** State claim, unit of analysis, primary outcome, uncertainty method, direction, tolerances, and decision rule before stress testing.
2. **Preregister perturbations.** Enumerate plausible families and severities, including where relevant noise, missingness, timing, scaling, thresholds, random seeds, and matched nulls. Add domain-specific adversarial counterexamples. Justify ranges independently of observed outcomes.
3. **Freeze comparators.** Use conventional baselines with matched inputs, information access, compute budget where practical, tuning allowance, splits, and metrics. Explain unavoidable mismatches.
4. **Execute the complete grid.** Include every registered family × severity × seed × method cell. Report failures, invalid runs, exclusions, and deviations; never drop inconvenient cells without a declared rule.
5. **Summarize envelope.** Report per-condition performance and uncertainty, worst case, best case, aggregate, variability, and candidate-minus-baseline differences. Keep conditions visible; do not hide severe cases inside a mean.
6. **Find first failure boundary.** Within each ordered severity family, report the earliest preregistered severity where the primary tolerance is violated, with the metric and comparator at that point. If none, report “not observed within tested range,” not “unbreakable.”
7. **Classify.** Apply the preregistered tolerance gate. Unregistered tolerances cannot rescue a failed result.

## Perturbation families (choose and justify before outcomes)

| Family | Example severity axis |
|---|---|
| Noise | SNR, corruption fraction, structured vs. iid noise |
| Missingness | Missing fraction, burstiness, missing-not-at-random mechanism |
| Timing | Jitter, delay, drift, sampling-rate shifts, window offsets |
| Scaling | Unit conversion, amplitude/normalization, feature scale, calibration shift |
| Thresholds | Predeclared threshold sweep or decision-boundary displacement |
| Seeds | Fixed registered seed set; report all runs, not best seed |
| Nulls | Matched null inputs, shuffled labels, placebo signal, negative controls |
| Adversarial counterexamples | Plausible boundary or constructed cases that should falsify the stated claim |
| Domain-specific | Named and operationalized by the investigator before testing |

Do not perturb irrelevant dimensions merely to inflate test count. Conversely, do not omit a plausible nuisance family because preliminary results look poor.

## Gate rules

- **PASS** only if all mandatory preregistered cells satisfy declared tolerances and the baseline comparison is complete and matched as specified.
- **FAIL** if any mandatory cell exceeds tolerance, a declared null produces the claimed effect beyond its allowed rate, an adversarial counterexample contradicts the claim, or success is confined to a narrow setting.
- **N/A** if the preregistration, baseline, metric, outcome record, or material cell provenance is missing. Missing evidence never counts as a passed perturbation.
- Report first failure boundary per perturbation family. “No failure observed” is bounded by the tested range.

## Repository contents

- `animal.yaml`: concise operation card and gate logic.
- `schemas/report.schema.json`: machine-readable report contract.
- `templates/preregistration.json`: freeze before running.
- `templates/stress-report.json`: fill-in report.
- `examples/demo-report.json`: illustrative failing stress test.
- `src/monster.py`: standard-library report gate checker and envelope helper.
- `tests/`: gate and envelope behavior tests.

## Validate a report

Requires Python 3.10+; no third-party packages.

```sh
python -m unittest discover -s tests -v
python src/monster.py templates/stress-report.json
python src/monster.py examples/demo-report.json
```

The checker verifies declared gate logic, not scientific truth or completeness. The full registered grid and raw run artifacts must be independently inspectable.

## Report minimum

Record frozen target and preregistration ID, metric/tolerance, each family and severity, seeds, matched baseline, per-cell results, full performance envelope, first failure boundary, deviations, and decision. See schema and templates.

## Scope boundary

MONSTER tests **survival under hostile conditions**. It does not establish that labels or evidence were built independently or without leakage. Use CIRCUS for provenance and circular support; use other Zoo animals for their specified proof, dimensional, novelty, or empirical operations.

## License

CC0-1.0. See `LICENSE`.
