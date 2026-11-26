---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/ThetaSpanRationalTranslatesVacuum.lean",
  "declarations": [
    "GlobalTheory.ThetaSpan.theta_span"
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

## Spanning by rational translates of a theta function

[Theorem THETA.1402](https://andrewodesky.com/rh/lean/GlobalTheory.ThetaSpan.theta_span/)

Fix the source's full arithmetic datum, including the CM field $E$, its associated imaginary quadratic field $K$, an allowed ideal $\mathfrak c\subset\mathcal O_K$, and a complex number $\delta$ satisfying the curve-ideal and discriminant-twelfth-root conditions. Fix $N,N'\ge0$. The associated standard theta datum supplies a complex vector space $V$, period lattice $\Lambda$, Hermitian form $H$, semicharacter $\alpha$, and quadratic phase $q$. Define $$U_zf(w)=f(w+z)\exp\!\left(-\pi H(w,z)-\frac\pi2H(z,z)\right),\qquad W_zf=e^{\pi i q(z)}U_zf.$$ Let $e_0\ne0$ be holomorphic and satisfy $\alpha(z)U_ze_0=e_0$ for every $z\in\Lambda$. If $F:V\to\mathbb C$ is holomorphic and, for some integer $m\ge1$, $$W_{mz}F=F\qquad(z\in\Lambda),$$ then there are finitely many $r_j\in\mathbb C$ and $Z_j\in M_{N'\times N}(E)$ such that $$F=\sum_jr_jW_{\delta\iota(Z_j)}e_0.$$ Here $\iota$ is the embedding of matrices through the selected CM embeddings supplied by the datum.
