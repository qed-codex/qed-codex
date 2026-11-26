---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/EisensteinSeriesLeftInvariance.lean",
  "declarations": [
    "GlobalTheory.T.eisenstein_series_left_invariance"
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

## Continuity and moderate growth of convergent Eisenstein sums

[Theorem AGR.1538](https://andrewodesky.com/rh/lean/GlobalTheory.T.eisenstein_series_left_invariance/)

Let $E/F$ be number fields and $\sigma\in\operatorname{Aut}_F(E)$. Fix the source's base datum with its additional CM, imaginary-quadratic-subfield, finite-unramifiedness and additive-character conditions, and a Hermitian or skew-Hermitian space $Y$ of rank $n\ge1$ with the prescribed signature and lattice conditions. Let $G=U(2Y)$ and choose the source's split frame, associated standard compact subgroup $K$, and Iwasawa height $a$, characterized by $a(pk)=|\det t|_{\mathbb A_E}$ for Siegel-parabolic Levi component $t$ and $k\in K$. Let $\chi:\mathbb A_E^\times\to S^1$, $s_1\in\mathbb C$, and let $f:G(\mathbb A_F)\to\mathbb C$ be continuous, right $K$-finite, and satisfy $$f(px)=\chi(\det t)|\det t|_{\mathbb A_E}^{s_1+n/2}f(x).$$ Put $f_s(x)=a(x)^{s-s_1}f(x)$. There is $t_0\in\mathbb R$ such that, for every $t\ge t_0$ and every family $\mathcal E(s,x)$ satisfying $$\sum_{\gamma\in P(F)\backslash G(F)}f_s(\gamma x)=\mathcal E(s,x)\qquad(\operatorname{Re}s>t),$$ with convergence as an unordered sum, $\mathcal E$ is jointly continuous there. For every $c,c'\in\mathbb R$ with $t<c$, there are $C\in\mathbb R$, $N\ge0$ with $$|\mathcal E(s,x)|\le C H(x)^N\qquad(c\le\operatorname{Re}s\le c',\ x\in G(\mathbb A_F)).$$ For every $\operatorname{Re}s>t$, the function $\mathcal E(s,\cdot)$ lies in the complex span of continuous functions bounded by some integral power of the prescribed matrix height $H$.
