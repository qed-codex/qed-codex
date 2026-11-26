---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/ZetaCharacterDivisibility/DivisionOneGeometricRepresentation.lean",
  "declarations": [
    "UpperTheory.Gal.Int.Div.divSet_holds",
    "UpperTheory.Gal.Int.Div.senWLac_holds"
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

## Extracting a Galois subrepresentation from dense polynomial data

[Theorem AGR.0088](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.Div.divSet_holds/)

Let $E$ be a number field, $\Omega$ an algebraic closure of $E$, $\ell$ a prime, and $$\rho:G_E\longrightarrow\mathrm{GL}_{d}(\overline{\mathbb Q}_\ell)$$ a continuous semisimple representation. Fix $a\ge0$. Assume the local Hodge comparison conditions of ([Separated Hodge jumps give separated Lie algebra eigenvalues](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.Div.senWLac_holds/)): at some prime above $\ell$, compatible local period and comparison data yield a filtration-jump multiset containing a set $J_0$ of $a$ integers such that any two disjoint nonempty subsets of $J_0$ have different averages.

Let $\psi:G_E\to\overline{\mathbb Q}_\ell^\times$ be continuous. Suppose the elements $g\in G_E$ for which there is a monic polynomial $Q_g$ of degree $a$ satisfying $$Q_g(\rho(g))=0,\qquad\psi(g)=(-1)^a Q_g(0)$$ are dense. Then there is a continuous semisimple representation $r:G_E\to\mathrm{GL}_a(\overline{\mathbb Q}_\ell)$ admitting an injective equivariant map into $\rho$, such that $\rho$ admits an injective equivariant map into a finite direct sum of copies of $r$. In addition, $$\{g\in G_E:\det(T-r(g))\text{ is separable}\}$$ is open and dense.

## Separated Hodge jumps give separated Lie algebra eigenvalues

[Theorem PHT.1426](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.Div.senWLac_holds/)

Let $E$ be a number field with algebraic closure $\Omega$, let $\ell$ be a rational prime, and let $N,n\ge0$. Let $V:G_E\to\operatorname{GL}_N(\overline{\mathbb Q}_\ell)$ be continuous, where $G_E=\operatorname{Gal}(\Omega/E)$. Assume the local period and comparison-bridge conditions in ([Hodge jumps under uniform trace approximation](https://andrewodesky.com/rh/lean/GlobalTheory.LimitTop.closedAtL/)) at some place above $\ell$: a tied local period-ring system, an induced local comparison bridge, an embedding $\tau:E\to\overline{\mathbb Q}_\ell$, and a multiset $J$ of filtration jumps for the restriction of $V$. Suppose there are distinct $k_1,\ldots,k_n\in J$ such that disjoint nonempty subsets have different averages: $$|B|\sum_{i\in A}k_i\ne|A|\sum_{i\in B}k_i\qquad(A,B\subset\{1,\ldots,n\},\ A,B\ne\varnothing,\ A\cap B=\varnothing).$$ There exist an algebraically closed extension $K'/\overline{\mathbb Q}_\ell$ and $X\in\operatorname{Lie}(\overline{V(G_E)}^{\mathrm{Zar}})(K')$ whose characteristic polynomial has distinct roots $e_1,\ldots,e_n\in K'$ satisfying the same subset-average inequalities.
