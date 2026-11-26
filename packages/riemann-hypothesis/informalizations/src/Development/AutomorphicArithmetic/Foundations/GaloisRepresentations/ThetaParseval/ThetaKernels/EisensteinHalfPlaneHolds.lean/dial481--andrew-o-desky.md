---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/EisensteinHalfPlaneHolds.lean",
  "declarations": [
    "GlobalTheory.T.eisenstein_half_plane_holds"
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

## Holomorphic Eisenstein sums in a right half-plane

[Theorem ANT.1676](https://andrewodesky.com/rh/lean/GlobalTheory.T.eisenstein_half_plane_holds/)

Let $E/F$ be number fields with an $F$-automorphism $\sigma$, and fix the base datum of ([Convergence and polynomial growth of a height Eisenstein sum](https://andrewodesky.com/rh/lean/GlobalTheory.T.eisenstein_series_convergence_bound/)), satisfying the CM, imaginary-quadratic-subfield, finite-unramifiedness, standard-additive-character, and local-character conditions stated there. Let $Y$ have rank $n\ge1$ and satisfy either its Hermitian or its skew-Hermitian signature-and-lattice conditions, with some signatures $(r,s)$. Let $\chi:\mathbb A_E^\times\to S^1$ be a Hecke character and $c\ge0$, and assume its restriction to $\mathbb A_F^\times$ is $\eta^c$, where $\eta$ is the quadratic character given by membership in $F^\times N_{E/F}(\mathbb A_E^\times)$.

Put $G=U(Y\oplus(-Y))$. Choose a permitted isotropic frame $b$ of this doubled space, a compatible standard compact subgroup $K\subset G(\mathbb A_F)$, and its prescribed height $h$. For every section $f$ of the induced representation defined in ([Continuity and moderate growth of convergent Eisenstein sums](https://andrewodesky.com/rh/lean/GlobalTheory.T.eisenstein_series_left_invariance/)) at a parameter $s_1\in\mathbb C$, there are $t\in\mathbb R$ and a family $v(s)$ of functions on $G(\mathbb A_F)$ such that, for $\Re s>t$ and every $x$, $$\sum_{\gamma\in P(F)\backslash G(F)}f_s(\gamma x)=v(s)(x),$$ with convergence as an unordered sum. Here $f_s=h^{s-s_1}f$ is the flat section of ([Continuity and moderate growth of convergent Eisenstein sums](https://andrewodesky.com/rh/lean/GlobalTheory.T.eisenstein_series_left_invariance/)), and $P$ is the parabolic determined by $b$. The family $v$ is weakly holomorphic on $\Re s>t$ for the growth functionals defined in ([Meromorphic Eisenstein families tested by growth functionals](https://andrewodesky.com/rh/lean/PositivityTheory.SiegelWeilFormula.Aeis.eisBLW/)).
