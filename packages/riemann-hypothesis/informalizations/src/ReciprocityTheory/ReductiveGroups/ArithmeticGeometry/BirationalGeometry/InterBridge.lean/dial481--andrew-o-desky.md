---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/InterBridge.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.G.Geo.resBridge"
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

## A logarithmic intersection integral on an analytic resolution

[Theorem ARAK.1357](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.resBridge/)

Let $K$ be nonempty finite, let $(I_k)_{k\in K}$ be finite sets, and put $R=\mathbb Z[x_{k,i}]$. Let $P,J\subseteq R$ be ideals, let $e\ge0$, and assume that $P$ defines a relevant horizontal integral arithmetic multiprojective variety of arithmetic dimension $e+1$. Fix an analytic logarithmic resolution of $(P,J)$ satisfying the conditions in the conventions, with compact Hausdorff complex manifold $Y$ of dimension $e$ and compatible local lifts $\gamma_y$ into the nonzero-block complex cone of $P$. Let $\Psi$ be a linear projection of its Segre coordinates to $\mathbb C^{e+1}$ that is nonzero on every point of the nonzero-block cone.

Let $L_1,\ldots,L_e,A$ be smooth Hermitian multidegree line data on the cone, and let $s\in R$ be a section of $A$ along $P$. Write $h_j$ for the metric functions of $L_j$ and $\log\|s\|_A=\log(|s|/h_A)$. Then $$I_{P,\Psi}\bigl(\log h_1,\ldots,\log h_e;\log\|s\|_A\bigr) =\int_Y\log\|s(\gamma_y(y))\|_A\;\bigwedge_{j=1}^e dd^c\log h_j(\gamma_y),$$ where $dd^c=(i/\pi)\partial\bar\partial$, and $I_{P,\Psi}$ is the source's sheet integral: integrate the mixed-curvature density times the displayed logarithm over the finite fibres of the affine chart of $\Psi$.
