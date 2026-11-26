---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/SemiabelianSchemes/AbelianSchemeQuotients/IsAbelianScheme.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.G.Semi.IsAbelianScheme",
    "ReciprocityTheory.ChartRestriction.G.Semi.IsSemiAbelian",
    "ReciprocityTheory.ChartRestriction.G.Semi.TorusExtension"
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

## Abelian and semiabelian group schemes

[Definition / hypothesis AV.D003](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Semi.IsAbelianScheme/)

An *abelian scheme* over a scheme $S$ is a commutative group scheme $A\to S$ whose structural morphism is smooth, proper and geometrically connected.

For a free abelian group $X$ of finite rank, the *split torus with character group $X$* over $S$ is $$T_{X,S}=S\times_{\operatorname{Spec}\mathbb Z}\operatorname{Spec}\mathbb Z[X].$$ Here $\mathbb Z[X]$ has basis $e^x$ for $x\in X$, with $e^xe^y=e^{x+y}$. Its group law, identity and inversion are given by $e^x\mapsto e^x\otimes e^x$, $e^x\mapsto1$ and $e^x\mapsto e^{-x}$, respectively. Rank zero is allowed.

A *semiabelian scheme* over $S$ is a commutative group scheme $G\to S$ whose structural morphism is smooth, separated, quasi-compact and geometrically connected, with the following property at every geometric point $s:\operatorname{Spec}\Omega\to S$. There are a free abelian group $X$ of finite rank, an abelian scheme $A$ over $\Omega$, and group homomorphisms $$T_{X,\Omega}\xrightarrow{i}G_s\xrightarrow{q}A$$ such that $q$ is flat, surjective and quasi-compact, and the square $$\begin{matrix} T_{X,\Omega}&\xrightarrow{i}&G_s\\ \downarrow&&\downarrow q\\ \operatorname{Spec}\Omega&\xrightarrow{e_A}&A \end{matrix}$$ is Cartesian, where $e_A$ is the identity section of $A$. Thus $i$ identifies the torus with the scheme-theoretic kernel of $q$. The field $\Omega$ ranges over all algebraically closed fields, and the choices of $X,A,i,q$ may depend on $s$.
