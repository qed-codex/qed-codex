---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/HasComplementOfBasis.lean",
  "declarations": [
    "GlobalTheory.UnitPerp.unitVectorPerpOver"
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

## Vectors of norm 1 and -1 with self-dual integral complements

[Theorem AV.1620](https://andrewodesky.com/rh/lean/GlobalTheory.UnitPerp.unitVectorPerpOver/)

Let $E$ be a CM number field with complex conjugation $a\mapsto\bar a$. Assume that for each maximal ideal $\mathfrak p\subseteq\mathcal O_E$ there is $\theta\in\mathcal O_E$ with $\theta-\bar\theta\notin\mathfrak p$. Let $W$ be a Hermitian $E$-space in the generic definition of ([Hermitian spaces in the theta constructions](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.CMData/)), and write $h$ for its form. Suppose $\dim_EW=M\ge3$ and that, at every embedding $E\hookrightarrow\mathbb C$, its signature label is $(P,Q)$ and equals the actual signature of the form.

If $P\ge1$, there is $x\in W$ with $h(x,x)=1$; if $Q\ge1$, there is $x\in W$ with $h(x,x)=-1$. In either case there is a self-dual full $\mathcal O_E$-lattice $L\subseteq W$ containing $x$ and satisfying $$L=\mathcal O_Ex+(L\cap x^\perp).$$ There is also a Hermitian space $W'$ isometrically embedded onto $x^\perp$, taking its distinguished lattice to $L\cap x^\perp$, with signatures respectively $(P-1,Q)$ and $(P,Q-1)$ and dimension $M-1$.
