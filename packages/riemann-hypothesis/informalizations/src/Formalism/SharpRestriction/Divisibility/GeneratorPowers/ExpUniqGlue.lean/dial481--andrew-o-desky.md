---
{
  "module": "src/Formalism/SharpRestriction/Divisibility/GeneratorPowers/ExpUniqGlue.lean",
  "declarations": [
    "Formalism.MainNotions.ModuliIntegralCharts.H1.ExpUniqGlue.expUniqRaw"
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

## Uniqueness of formal group homomorphisms from their tangent vectors

[Theorem AV.0326](https://andrewodesky.com/rh/lean/Formalism.MainNotions.ModuliIntegralCharts.H1.ExpUniqGlue.expUniqRaw/)

Let $E$ be a CM field and fix the source's polarized unitary moduli datum, level, moduli scheme $X$, and universal semiabelian group $A/X$. Let $S$ be a commutative $\mathbb Q$-algebra, $x_0:\operatorname{Spec}S\to X$, $d\ge0$, and $$S_m=S[t_1,\ldots,t_d]/(t_1,\ldots,t_d)^{m+1}.$$ Let $x_m,x'_m\in A_{x_0}(S_m)$ be two systems compatible with truncation. Suppose each system satisfies the additive formal group law: after substitution into the ring truncated in total degree at $m$, its value at $t+u$ is the product of its values at $t$ and $u$. If, for every $1\le j\le d$, the two $S[\epsilon]/(\epsilon^2)$-points obtained from $x_1,x'_1$ by $t_j\mapsto\epsilon$ and $t_i\mapsto0$ for $i\ne j$ agree, then $$x_m=x'_m\qquad(m\ge0).$$
