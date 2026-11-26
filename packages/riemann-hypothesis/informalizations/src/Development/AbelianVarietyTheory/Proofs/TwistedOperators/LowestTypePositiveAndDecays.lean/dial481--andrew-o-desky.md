---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/LowestTypePositiveAndDecays.lean",
  "declarations": [
    "GlobalTheory.SphJet.lowest_type_positive_and_decays"
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

## Positivity and decay of lowest-type discrete-series coefficients

[Theorem REP.1395](https://andrewodesky.com/rh/lean/GlobalTheory.SphJet.lowest_type_positive_and_decays/)

For every pair of nonnegative integers $p,q$, use two ordered index blocks of sizes $p,q$ and fix a topological group model $$\widetilde U(p,q)=\{(g,w):g\in U(p,q),\ w\in\mathbb C^\times,\ w^2=\det g\},$$ with Haar measure, and let $K$ be the inverse image of $U(p)\times U(q)$. Use the specified continuous lift $\widetilde{\exp}:\mathfrak u(p,q)\to\widetilde U(p,q)$ of the matrix exponential, with $\widetilde{\exp}(0)=1$ and $$\widetilde{\exp}((s+t)Y)=\widetilde{\exp}(sY)\widetilde{\exp}(tY)\quad(s,t\in\mathbb R).$$ For every rational vector $\lambda$ on the two blocks, fix a member $\pi_\lambda$ of a family of nonzero irreducible strongly continuous unitary representations, with algebraic realizations and discrete-series orthogonality as specified below. For every quadruple of nonnegative integers $p,q,r,s$, also fix the compatible oscillator realization specified in the conventions. Assume the Blattner, Harish–Chandra, tensor-weight and induced-module hypotheses below.

Call a rational vector $\lambda$ admissible if it is injective, strictly decreasing within each block, has half-integral entries, and has integral pairwise differences. Define its Blattner weight by $$\Lambda_a=\lambda_a+\frac12\left(\sum_{b\text{ in the opposite block}}\operatorname{sgn}(\lambda_a-\lambda_b)-\sum_{b\text{ in the same block}}\operatorname{sgn}(\lambda_a-\lambda_b)\right).$$ Let $V_{\mathrm{low}}$ be the image in the Hilbert representation of all algebraic vectors that lie in a finite-dimensional $\mathfrak k_{\mathbb C}$-stable subspace whose nonzero compact highest-weight vectors all have weight $\Lambda$.

Suppose $\lambda$ is admissible and every difference of entries in opposite blocks has absolute value at least $h$, where $$h\ge120(p+q)\min(p,q)^{3/2}.$$ Let $\mathfrak p$ consist of the matrices $Y=\begin{pmatrix}0&B\\B^*&0\end{pmatrix}$. For $Y\in\mathfrak p$ and $x\in V_{\mathrm{low}}$, $$\langle x,\pi_\lambda(\widetilde{\exp}Y)x\rangle\in[0,\infty),$$ and for $k\in K$ and $x,y\in V_{\mathrm{low}}$, $$|\langle y,\pi_\lambda(k\widetilde{\exp}Y)x\rangle|\le\exp\!\left[-\frac h8\min\!\left(\|Y\|_{\mathrm{HS}}^2,\frac{\|Y\|_{\mathrm{HS}}}{\sqrt{2\min(p,q)}}\right)\right]\|x\|\,\|y\|.$$ Here $\|Y\|_{\mathrm{HS}}^2=\sum_{a,b}|Y_{ab}|^2$, and division by zero is taken to be zero.
