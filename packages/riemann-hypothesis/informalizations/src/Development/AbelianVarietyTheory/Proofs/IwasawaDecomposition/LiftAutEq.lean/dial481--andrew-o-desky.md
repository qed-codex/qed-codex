---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/LiftAutEq.lean",
  "declarations": [
    "GlobalTheory.Mem.Lift.liftAutEq"
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

## Convergence and smooth automorphy of an equal-rank theta lift

[Theorem THETA.0799](https://andrewodesky.com/rh/lean/GlobalTheory.Mem.Lift.liftAutEq/)

Assume the rapid-decay input for smooth uniformly moderate cuspidal forms stated in the conventions below. Fix its full CM unitary arithmetic datum, compatible infinite embeddings $\theta$ and an additive character $\psi$ with the negative standard infinite normalization in ([Convergence and polynomial growth of a height Eisenstein sum](https://andrewodesky.com/rh/lean/GlobalTheory.T.eisenstein_series_convergence_bound/)). Let $V,W$ have equal rank $n$, and let $\chi,\chi'$ be Hecke splitting characters with integral infinity exponents and the restriction condition below. Let $\omega$ be a Weil action for these data, let $\mu$ be a Haar measure on $U(V)(\mathbb A)$ and $\mathcal F$ a fundamental domain for $U(V)(F)$ acting by left multiplication.

For every theta vector $\Phi$ in the theta model defined in the conventions below and every smooth cuspidal automorphic form $F$ with the conditions stated there on $U(V)(\mathbb A)$, the function $$g\longmapsto (\omega(g,h)\Phi)(0)F(g)$$ is integrable on $\mathcal F$ for every $h\in U(W)(\mathbb A)$. Moreover, $$h\longmapsto\int_{\mathcal F}(\omega(g,h)\Phi)(0)F(g)\,d\mu(g)$$ is a smooth automorphic function of uniformly moderate growth, with finite open level and a finite-dimensional orbit under the specified central Lie operators.
