---
{
  "module": "src/Formalism/PeriodIntegrals/OrbitalBoundsConclusion/WittExtensionTheorem.lean",
  "declarations": [
    "witt_extension_theorem"
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

## Extension of an isometry of a subspace

[Theorem ALG.0711](https://andrewodesky.com/rh/lean/witt_extension_theorem/)

Let $K$ be a field of characteristic zero with an involution, and let $V$ be a finite-dimensional $K$-vector space. Let $B:V\times V\to K$ be sesquilinear, conjugate-linear in the first argument, such that $$\overline{B(x,y)}=B(y,x),\qquad \bigl(B(x,y)=0\text{ for all }y\bigr)\Longrightarrow x=0.$$ If $U\subset V$ is a subspace and $f:U\to V$ is an injective $K$-linear map satisfying $B(fx,fy)=B(x,y)$ for all $x,y\in U$, then there is $g\in\operatorname{GL}_K(V)$ satisfying $$B(gx,gy)=B(x,y)\quad(x,y\in V),\qquad g|_U=f.$$
