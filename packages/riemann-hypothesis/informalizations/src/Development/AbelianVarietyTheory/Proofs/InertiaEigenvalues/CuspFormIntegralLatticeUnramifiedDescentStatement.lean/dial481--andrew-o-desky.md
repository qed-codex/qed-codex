---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CuspFormIntegralLatticeUnramifiedDescentStatement.lean",
  "declarations": [
    "GlobalTheory.T.cuspForm_integral_lattice_unramified_descent"
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

## Descent of an integral cusp lattice across an unramified coefficient extension

[Theorem AV.1041](https://andrewodesky.com/rh/lean/GlobalTheory.T.cuspForm_integral_lattice_unramified_descent/)

Fix the source's CM unitary moduli datum: a CM field $E$, the CM lattice datum specified in the conventions of ([Nonzero Gram determinant and bases away from finitely many primes](https://andrewodesky.com/rh/lean/GlobalTheory.T.gram_det_ne_zero_local_basis_cofinite/)), a level with integer $M$, representing moduli scheme $X$, and coefficient number field $F$. Choose the full complex uniformization data below, indexed by embeddings $F\hookrightarrow\mathbb C$. Let $\lambda$ be a finite prime of $F$ over a rational prime $p$, and assume $$M/p^{v_p(M)}\ge3.$$ Let $F'\supseteq F$ be another permitted coefficient field and $\lambda'$ a finite prime of $F'$ whose normalized additive valuation restricts to $v_\lambda$ on $F$. Assume cusp forms over $F'$ are spanned by base changes of cusp forms over $F$, for every weight and nonnegative twisting degree.

Fix nonnegative weight sequences $a_{\tau,0}\ge a_{\tau,1}\ge\cdots$ for each embedding $\tau:E\hookrightarrow\mathbb C$, and a nonnegative even integer $n$. Suppose the corresponding cusp-form space over $F$ is finite-dimensional. If $f'$ is a cusp form of this weight and degree over $F'$ integral in the sense below, there are finitely many cusp forms $f_j$ of the same weight and degree over $F$ and scalars $c_j\in F'$ such that $$|c_j|_{\lambda'}\le1,\qquad f'\text{ is represented by }\sum_jc_jf_j$$ after evaluation on every common coefficient-algebra point, and every $f_j$ is integral at $\lambda$ in the same sense.
