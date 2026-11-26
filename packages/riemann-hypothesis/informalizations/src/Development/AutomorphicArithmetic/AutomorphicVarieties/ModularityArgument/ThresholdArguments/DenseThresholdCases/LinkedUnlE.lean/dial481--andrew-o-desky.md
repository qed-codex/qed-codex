---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/LinkedUnlE.lean",
  "declarations": [
    "UpperTheory.V.Z.J.count_i_of_printed_bound_k_kato_automorphy",
    "UpperTheory.V.Z.J.count_v_of_printed_bound_k_reduced_unitary_lift"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## Automorphic and cohomological inputs for localization bounds

[Theorem GC.1745](https://andrewodesky.com/rh/lean/UpperTheory.One.Join.automorphic_window_of_inputs/)

Assume ([Galois representations of polarized cusp forms](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter/)), with all its local comparison hypotheses and conventions, and ([Base change from a definite unitary group](https://andrewodesky.com/rh/lean/UpperTheory.BaseChangeIdentities.baseChangeN/)). Then the following assertions hold.

1. The condition in ([Normalized Poitou–Tate duality for finite Galois modules](https://andrewodesky.com/rh/lean/GlobalTheory.Published.PoitouTateDuality/)), ([Local cohomology finiteness and dimension](https://andrewodesky.com/rh/lean/CompanionTheory.LocalTateOrthogonality.Gcoh.top_locfin/)), ([Local Tate duality](https://andrewodesky.com/rh/lean/CompanionTheory.LocalTateOrthogonality.Gcoh.top_tate/)), ([Class-group ranks in cyclotomic towers](https://andrewodesky.com/rh/lean/UpperTheory.V.FW.ferreroWashington/)), and the existence of a real constant satisfying the condition in ([A uniform bound for second cyclotomic cohomology](https://andrewodesky.com/rh/lean/UpperTheory.V.LemmaK/)) all hold, with the quantifiers and normalizations specified by these titles.
2. All five uniform character estimates I, II, III, V and Z in the conventions of ([Positive localization lengths from character estimates](https://andrewodesky.com/rh/lean/UpperTheory.V.HV.pointHV_of_counts/)) hold, including their case conditions, finiteness assertions, quantifiers and dependence of constants. The Poitou–Tate, local finiteness, local Tate duality and second-cohomology hypotheses of ([Positive localization lengths from character estimates](https://andrewodesky.com/rh/lean/UpperTheory.V.HV.pointHV_of_counts/)) also hold.
3. The universal Bernoulli character-eigenspace hypothesis in the conventions of ([Summing the negative localization lengths](https://andrewodesky.com/rh/lean/UpperTheory.V.Odd.thmBcFree_of/)) holds, with its coefficient rings, parity, integrality condition and valuation normalization.

The condition in ([Window condition: a bound on the Tate-Shafarevich groups of the twists Q\_l/Z\_l(-k) over auxiliary abelian fields](https://andrewodesky.com/rh/lean/UpperTheory.Top.VWin/)) also holds.

## A bound for sums of Selmer lengths of twisted Dirichlet characters over primes

[Theorem GC.1.1766](https://andrewodesky.com/rh/s/p054-weighted-selmer-length-bound.html)

Assume the following four hypotheses.

- (A) The fifteen statements of ([Hypothesis list D: fifteen assumed statements on cuspidal automorphic representations of general linear groups, base change, descent to unitary groups and Galois representations](https://andrewodesky.com/rh/lean/UpperTheory.V.Af.HypothesesH'/)).
- (B) A uniform bound holds in the sense of ([A uniform bound for second cyclotomic cohomology](https://andrewodesky.com/rh/lean/UpperTheory.V.LemmaK/)).
- (C) The conclusion of ([Vanishing of two rank-two Selmer groups](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.Kato.WeilSphericalRecords.katoTwoW_of_printsH/)) holds for all data that satisfy conditions 1–10 of that theorem.
- (D) The assumption of ([An automorphy assumption for specializations with unramified coefficients](https://andrewodesky.com/rh/lean/UpperTheory.V.Aut.AutomorphyUnramifiedCoefficientsAlt/)) holds.

The constants $N_\chi$, $o$, $p_K$, $h_K$ and $p_1$ of a primitive Dirichlet character $\chi$, its set of primes $\mathcal B_\chi$, the auxiliary triples $(\nu,q,d)$ for $\chi$, the modulus $N$ of such a triple and the sets $\mathscr X_{\mathcal O}(e)$ of Dirichlet characters modulo $N$ are defined in ([Auxiliary moduli of a primitive Dirichlet character and their characters](https://andrewodesky.com/rh/lean/Formalism.HC.PChar/)). The Selmer length of a character $(\epsilon_\ell^e\psi)^{-1}$ formed with a ring $\mathcal O$ and a modulus $N$, and the number $e_{\mathcal O}$, are defined in ([Selmer lengths of twisted Dirichlet characters and Estimate I](https://andrewodesky.com/rh/lean/UpperTheory.V.HV.CountI/)).

Let $\chi$ be a primitive Dirichlet character. Then there are a natural number $C$ and primes $r_1$ and $r_2$ with the following property.

Let $(\nu,q,d)$ be an auxiliary triple for $\chi$, with modulus $N$, such that $q$ and $d$ are both larger than $r_1$ and $r_2$. Let $t\ge0$ be an integer such that $q$ and $d$ are both larger than each of the six numbers $$2t+1,\qquad N_\chi,\qquad o,\qquad p_K,\qquad h_K,\qquad p_1,$$ and let $e$ be an integer with $0<e<t$. Let $\overline{\mathbb Q}$ be an algebraic closure of $\mathbb Q$. For every prime $\ell$ let $\mathcal O_\ell\subset\overline{\mathbb Q}_\ell$ be a discrete valuation ring that contains $\mathbb Z_\ell$ and is a finitely generated $\mathbb Z_\ell$-module. Let $S$ be a finite set of odd primes such that every $\ell\in S$ satisfies $$\ell\notin\mathcal B_\chi\qquad\text{and}\qquad(\ell-1)\nmid2e.$$ For $\ell\in S$ and $\psi\in\mathscr X_{\mathcal O_\ell}(e)$ write $L_{\ell,\psi}$ for the Selmer length of $(\epsilon_\ell^e\psi)^{-1}$ formed with $\mathcal O_\ell$ and $N$. Then every $L_{\ell,\psi}$ is finite, and $$\sum_{\ell\in S}\log\ell\sum_{\psi\in\mathscr X_{\mathcal O_\ell}(e)}\frac{L_{\ell,\psi}}{e_{\mathcal O_\ell}}\le(Nt)^C.$$
