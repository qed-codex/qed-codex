---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/OverIx.lean",
  "declarations": [
    "GlobalTheory.Mem.Top.Bl.GeoP",
    "GlobalTheory.Mem.Top.Bl.geoOf",
    "GlobalTheory.Mem.Top.Bl.anyGeometry",
    "GlobalTheory.Mem.Top.Bl.OverIx",
    "GlobalTheory.Mem.Top.Bl.LamAre",
    "GlobalTheory.Mem.Top.Bl.OAt",
    "GlobalTheory.Mem.Top.Bl.OX"
  ],
  "author": "dial481",
  "writer": "Claude Fable 5.2",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "CC-BY-4.0"
}
---

# Informalization of OverIx.lean: the geometry slot and the predicate `anyGeometry`

**This 53-line file defines a slot for a geometric condition and two predicates that can fill it. One of them, `anyGeometry`, is true for every input, and the checked proof builds on that one.** This page says what the definitions state and where the predicate is used. It does not assess whether the argument needs a geometric condition at this point. [OverIx.lean](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/OverIx.lean#L1-L53) · [Audit of the path from the final theorem](https://github.com/dial481/riemann-hypothesis-rosetta/blob/c336b98c7459dea5d7e3199f7d5433e2414e2ac8/results/anygeometry.md)

AI drafted this autoinformalization from the original source. It is open for mathematical review.

## What the file defines

| Lean name | In words |
|---|---|
| `GeoP` | The type of a geometry predicate. It takes a datum `D : D7`, a core `J` of `D` and a divisor datum `X`, and returns a proposition. [Line 14](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/OverIx.lean#L14) |
| `geoOf Q` | The demanding predicate. It holds when some positive integer `c` satisfies `IsGeoOf (Q D) J c X` and `X` satisfies `HasTrueSurf`. [Lines 16–17](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/OverIx.lean#L16-L17) · [IsGeoOf](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/LargeFor.lean#L78-L80) · [HasTrueSurf](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/SecondChernDegreeVanishesTrueSurfaces.lean#L346) |
| `anyGeometry` | The predicate that is `True` for every `D`, `J` and `X`. [Line 19](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/OverIx.lean#L19) |
| `OverIx Z σ c` | For every index `i`, the submodule `isot (i+1) σ` is contained in the complex span of the image under `Z.jW i` of the set `Wp i c`. [Lines 29–31](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/OverIx.lean#L29-L31) |
| `LamAre Z Xd` | There is a labelling `lab` of each `σ` by an index with two properties. If `σ` satisfies `OverIx` for some index, it does so for `lab σ`. For every `i`, every `σ` and every embedding `e` other than `embLL`, the number `Xd.logLam (i+1) σ e` is the logarithm of the corresponding value of `lam` when `isot (i+1) σ` is nonzero, and is $0$ when it is zero. [Lines 33–38](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/OverIx.lean#L33-L38) |
| `OAt Γ t X` | A record with two fields: `geo`, a proof that the predicate `Γ` holds at this datum, and `lam`, a proof of `LamAre`. [Lines 44–47](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/OverIx.lean#L44-L47) |
| `OX Γ` | The component that assigns the record type `OAt Γ` to each row datum. [Line 49](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/OverIx.lean#L49) |

## What `anyGeometry` does

The record `OAt Γ` asks for a proof of `Γ` in its `geo` field. When `Γ` is `anyGeometry`, that field asks for a proof of `True`, so it places no condition on `D`, `J` or `X`. The `lam` field is the same whichever predicate is chosen. [The two fields](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/OverIx.lean#L44-L47)

On the checked path the slot is filled with `geoCl anyGeometry`. `GeoCl Γ` is the closure of `Γ` under one step operation, and its base case needs only `Γ` itself. Since `anyGeometry` holds for every input, `geoCl anyGeometry` holds for every input as well. [Where the slot is filled](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/Prm1.lean#L20-L21) · [GeoCl](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/NotGeoClFalse.lean#L21-L24) · [geoCl](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/NotGeoClFalse.lean#L26) · [Base case as a lemma](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/NotGeoClFalse.lean#L28)

None of the five final theorems uses the demanding predicate: the compiled dependency data records no use of `geoOf`, `IsGeoOf` or `HasTrueSurf` in their closures. Elsewhere in the project `geoOf` does appear, for example as the conclusion of `geoOf_set`. [geoOf_set](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/NotLamAreShift.lean#L26-L28) · [Audit, reach and source occurrences](https://github.com/dial481/riemann-hypothesis-rosetta/blob/c336b98c7459dea5d7e3199f7d5433e2414e2ac8/results/anygeometry.md#reach-and-source-occurrences)

## Where the predicate sits in the proof

These figures come from the Rosetta audit, which reads James Shore’s compiled dependency data and the pinned source.

- `anyGeometry` is eight dependency edges from `riemannHypothesis`, and it lies in the dependency closure of all five final theorems.
- 29 declarations refer to it directly. Of the 48 declarations that depend on it, 24 lie in the closure of `riemannHypothesis`.
- The name occurs in 24 source files.

[The eight edges](https://github.com/dial481/riemann-hypothesis-rosetta/blob/c336b98c7459dea5d7e3199f7d5433e2414e2ac8/results/anygeometry.md#the-eight-edges) · [Direct callers and dependents](https://github.com/dial481/riemann-hypothesis-rosetta/blob/c336b98c7459dea5d7e3199f7d5433e2414e2ac8/results/anygeometry.md#direct-callers-and-transitive-dependents)

## What this does and does not show

Lean checked the theorem that `Main.lean` states, which is Mathlib’s `RiemannHypothesis`, and the proof uses only the three standard axioms. The audit establishes this for the proof as written. It did not test the proof with `geoOf` in the slot. [Audit summary and axioms](https://github.com/dial481/riemann-hypothesis-rosetta/blob/c336b98c7459dea5d7e3199f7d5433e2414e2ac8/results/anygeometry.md)

It does show that the slot, as filled on the checked route, accepts every input, and that the compiled closures of the five theorems contain none of `geoOf`, `IsGeoOf` and `HasTrueSurf`. A condition of the same kind stated under other names would not show up in that check. Whether the mathematics calls for such a condition is a question this file does not settle.

## Later change in the maintained repository

On 24 November 2026 the maintained repository merged a change by Visio-Vanitas that removes `GeoP`, `anyGeometry`, the `geo` field and the predicate argument of `OAt` and `OX`, and deletes the file that defines `GeoCl`. After it, `OAt` has the single field `lam`. By then `geoOf` was no longer in the file. This page describes the original source at the pinned commit, where all of them are present. [The change](https://github.com/leanprover-community/riemann-hypothesis/pull/466)

## Credits

Jenny Lorraine Nielsen identified the constant-True predicate. Frank Chu asked whether the path from `Main.lean` runs through it. Harry Tong independently found it in all five compiled dependency closures. [Nielsen’s paper](https://philarchive.org/rec/NIEIOT-2) · [Chu’s question](https://dev.to/frankchu/grh-proofs-geometry-is-fun-true-in-24-files-2n2b) · [Tong’s audit](https://github.com/harrytong/rh-verification/blob/16b88c701bd7abddd93d49a9896cd4daab41f680/stage1/code/RH_critics_dependency_findings.md#exact-witness-paths)
