---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/HomogeneousIdeals/IsDomainAndIsIntegrallyClosedAtPrimeOfSmoothOfCo.lean",
  "declarations": [
    "GlobalTheory.isDomain_and_isIntegrallyClosed_atPrime_of_smooth_of_comap",
    "GlobalTheory.isDomain_and_isIntegrallyClosed_atPrime_of_smooth_of_forall"
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

## Normal local rings under a smooth algebra map

[Theorem AG.0489](https://andrewodesky.com/rh/lean/GlobalTheory.isDomain_and_isIntegrallyClosed_atPrime_of_smooth_of_comap/)

Let $A\to B$ be a smooth homomorphism of commutative rings and let $\mathfrak p\subseteq B$ be prime. Put $\mathfrak q=\mathfrak p\cap A$. If $A_{\mathfrak q}$ is an integrally closed domain, then $B_{\mathfrak p}$ is an integrally closed domain.

In particular, if $A_{\mathfrak q}$ is an integrally closed domain for every prime ideal $\mathfrak q\subseteq A$, then $B_{\mathfrak p}$ is an integrally closed domain for every prime ideal $\mathfrak p\subseteq B$.
