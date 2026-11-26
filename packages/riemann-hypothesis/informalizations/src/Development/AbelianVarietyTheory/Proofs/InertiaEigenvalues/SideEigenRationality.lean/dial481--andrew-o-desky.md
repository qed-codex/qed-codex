---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SideEigenRationality.lean",
  "declarations": [
    "GlobalTheory.LargeO.exists_bigOk"
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

## A finite set of coefficients controlling fields of definition

[Theorem AGR.0803](https://andrewodesky.com/rh/lean/GlobalTheory.LargeO.exists_bigOk/)

Fix the source's full CM arithmetic datum, with CM field $E$, algebraic closure $\Omega$, rank $n$ and specified split primes. Assume that after deleting any finite set of primes, the arithmetic Frobenius lifts at the remaining split primes are dense in $G_E=\operatorname{Gal}(\Omega/E)$. Let $\ell$ be prime, $Q$ a finite set of finite primes of $E$, $\mathcal E$ a finite set of functions $c:(v,k)\mapsto c(v,k)\in\mathbb C$, and $\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C$ a field isomorphism.

There is a finite $S\subset\mathbb C$ such that every intermediate field $\mathbb Q_\ell\subseteq K\subseteq\overline{\mathbb Q}_\ell$ containing $\iota^{-1}(S)$ has the following property. For $c\in\mathcal E$, let $\rho:G_E\to\operatorname{GL}_n(\overline{\mathbb Q}_\ell)$ have continuous matrix entries and be semisimple. Suppose that for every split $v$ outside $Q$, the primes above $\ell$, and the datum's specified exceptional set $S_\ell$, every arithmetic Frobenius lift $\sigma$ above $v$ satisfies $$\iota\bigl(\det(T-\rho(\sigma))\bigr) =T^n+\sum_{k=1}^n(-1)^k(Nv)^{k(k-1)/2}c(v,k)T^{n-k}.$$ There exists $P\in\operatorname{GL}_n(\overline{\mathbb Q}_\ell)$ such that every matrix entry of $P^{-1}\rho(g)P$ belongs to $K$ for every $g\in G_E$.
