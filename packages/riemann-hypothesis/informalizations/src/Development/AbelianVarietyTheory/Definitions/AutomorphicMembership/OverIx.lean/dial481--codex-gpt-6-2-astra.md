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
  "writer": "Codex (GPT-6.2 Astra)",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "CC-BY-4.0"
}
---

# Two obligations for a row in OverIx.lean

To construct a term of `OAt Γ t X`, one must fill two fields. One tests the predicate supplied as the parameter `Γ`. The other checks whether a single choice of labels explains certain logarithmic values of `X`. The split is visible in the types of the fields themselves. [The record](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/OverIx.lean#L44-L47)

## What changes when the predicate changes

A predicate of type `GeoP` takes three arguments. The datum `D` determines the types of the next two, a core `J` and a divisor datum `X`. For `geoOf Q`, the core and divisor must satisfy `IsGeoOf` for some positive natural number and the kit `Q D`. There is a separate conjunct `HasTrueSurf X`. For `anyGeometry`, evaluating the predicate at any well-typed triple gives `True`. Thus with that choice, the `geo` field can always be filled by the proof of `True`. The `lam` field still has exactly the type `LamAre t.r.Z X`. [The predicate type and both definitions](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/OverIx.lean#L14-L19) · [The two field types](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/OverIx.lean#L44-L47)

## What one label must explain

For fixed `Z` and $\sigma$, think of testing a candidate index $c$. At each index $i$, take the image of `Wp i c` under `Z.jW i` and form its complex linear span. The test is whether this span contains the specified subspace `isot` at $(i+1,\sigma)$ for **every** $i$. This is `OverIx Z σ c`. [The containment](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/OverIx.lean#L29-L31)

`LamAre` asks for a function `lab` of $\sigma$. Whenever some candidate passes that test, the chosen index `lab σ` must pass it. There is no uniqueness requirement. The same choice also occurs in equations for `Xd.logLam`, for every $i$, every $\sigma$ and every embedding $e$ distinct from `embLL`. When the specified subspace is nonzero, the value is the real logarithm of `lam` evaluated using `lab σ` and the infinite place represented by $e$. When the subspace is zero, the value must be zero. Even if no candidate passes the span test for a particular $\sigma$, the equations still apply there. They form a separate conjunct after the implication about candidates. [Scope of the choice, implication and equations](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/OverIx.lean#L33-L38)

## A concrete instantiation

`OX Γ` takes the divisor datum `O.X` from the object argument `O`. The rows `t` are a separate argument with base `O.p0`, and the resulting type is `OAt Γ t O.X`. [The two arguments](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/NonzeroPlacesOverPrimes.lean#L112-L113) Later, `parametersOfDependence` passes `geoCl anyGeometry` to `parametersOfExtension`. The closure has a base constructor taking a proof of the underlying predicate. At every triple, supplying the proof of `True` therefore suffices for this closed predicate, without using the step constructor. This explains the geometric field in that instantiation. Constructing the other field still requires the common label and the equations above. [Packaging the record](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/OverIx.lean#L44-L49) · [The selected predicate](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/Prm1.lean#L20-L21) · [The closure constructors and base lemma](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/NotGeoClFalse.lean#L21-L28)

## The maintained version

On 24 November 2026, Visio-Vanitas’s change removed the geometry parameter and its field. In the merged version, constructing `OAt` requires the `lam` field alone. The two obligations described above belong to the pinned original. [Upstream change to the record](https://github.com/leanprover-community/riemann-hypothesis/pull/466)
