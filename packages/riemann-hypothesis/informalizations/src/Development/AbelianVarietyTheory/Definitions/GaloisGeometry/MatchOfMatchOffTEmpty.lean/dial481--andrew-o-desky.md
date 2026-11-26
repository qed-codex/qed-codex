---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/GaloisGeometry/MatchOfMatchOffTEmpty.lean",
  "declarations": [
    "GlobalTheory.Cong.DescOffT"
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

## Descent of a polarized cusp form on GL\_a to the definite unitary group

[Theorem AGR.1.1777](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Desc.desc/)

Let $E$ be a CM field with maximal totally real subfield $E^+$, let $\ell$ be a prime and let $a\ge1$ be an integer. Let $\eta$ be the quadratic Hecke character of $E^+$ attached to the extension $E/E^+$. Let $\pi$ be a cuspidal automorphic representation of $\mathrm{GL}_a(\mathbb A_E)$, and assume the following five conditions.

- (i) $\pi$ is regular algebraic.
- (ii) The pair $(\pi,\eta^a)$ is polarized.
- (iii) $-d$ is a square in $E$ for some positive integer $d$.
- (iv) The degree $[E^+:\mathbb Q]$ is even.
- (v) Every nonsplit finite place $w$ of $E$ is unramified over $E^+$ and does not divide $\ell$, and $\pi$ has a Satake multiset at $w$.

Then there is an automorphic representation $U$ of the definite unitary group $\mathcal U$ in $a$ variables over $E$ with the following three properties.

1. $U$ is unramified at every nonsplit finite place of $E$.
2. For every split finite place $w$ of $E$, every local component of $\pi$ at $w$ occurs in $U$ at $w$.
3. For every embedding $\tau\colon E\to\mathbb C$ and every weight $\lambda=(\lambda_0\ge\dots\ge\lambda_{a-1})$ that occurs in $U$ at $\tau$, $$\operatorname{Inf}_\tau(\pi)=\Bigl\{\lambda_k+\tfrac{a-1}2-k:\ 0\le k<a\Bigr\}.$$
