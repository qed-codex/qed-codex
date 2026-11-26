---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/StatementWithTransposeOfBranching.lean",
  "declarations": [
    "GlobalTheory.BranchFormula.integrality"
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

## Integral branching under scaling

[Theorem ALG.0120](https://andrewodesky.com/rh/lean/GlobalTheory.BranchFormula.integrality/)

Assume the following integral branching package for every $N=n+1$ and every pair of weakly decreasing integer weights $\lambda\in\mathbb Z^N$, $\sigma\in\mathbb Z^n$ with $\lambda_i\ge\sigma_i\ge\lambda_{i+1}$. Define $$A_i=\sigma_i-\lambda_{i+1},\quad B_i=\lambda_i-\sigma_i,\quad D_0=\sum_i A_i,\quad D_1=\sum_i\min(\lambda_i-\lambda_{i+1},D_0),\quad b=\sum_i\lambda_i-\sum_i\sigma_i,$$ $$R_i=[\lambda_{i+1},\min(\lambda_i,\lambda_{i+1}+D_0)]\cap\mathbb Z,\qquad c_{\lambda,\sigma}=\prod_i\prod_{v\in R_i\setminus\{\sigma_i\}}\prod_j(v-i-\sigma_j+j).$$ Let $\xi_{\lambda,\sigma}$ be the product of the leading $i\times i$ minors to powers $A_i$ and the minors with rows $1,\ldots,i-1,N$ and columns $1,\ldots,i$ to powers $B_i$. Put $M=(2(\lambda_1-\lambda_N+N))^{ND_1}$ and $B=M\sqrt{\dim\Delta_\lambda(\mathbb C^N)}$. The package requires all of:

1. $c_{\lambda,\sigma}\ne0$, $|c_{\lambda,\sigma}|\le M$, $\xi_{\lambda,\sigma}\ne0$, and $b=\lambda_1-D_0$.
2. There are polynomial maps $i:\nabla_\sigma\to\nabla_\lambda$ and $r:\Delta_\lambda\to\Delta_\sigma$, extended linearly on the ambient polynomial rings, preserving both the integral polynomial lattices and the indicated complex Weyl spaces. The map $r$ is nonzero, and $i$ takes the extremal polynomial to $c_{\lambda,\sigma}\xi_{\lambda,\sigma}$.
3. Both maps intertwine the upper-left $\mathrm{GL}_n$ action. Scaling the last coordinate by $t$ acts on $i$ with weight $t^b$ and gives $r\circ\rho_\lambda(\operatorname{diag}(1,\ldots,1,t))=t^b r$.
4. Both maps have squared Fischer norm at most $B^2$, and they are transposes for the Fischer pairings: $\langle i(s),f\rangle_\lambda=\langle s,r(f)\rangle_\sigma$.

Let $K$ be a number field, $I$ finite, and let such pairs $(\lambda_\tau,\sigma_\tau)$ be given for $\tau\in I$. Require equal determinant shifts: the last coordinates of the two weights agree, with shift zero for an empty weight. Write $b_\tau=\sum_i\lambda_{\tau,i}-\sum_i\sigma_{\tau,i}$.

For clarity, the standard branching map $r_0$ used here extracts the coefficient with last-row exponents $B_{\tau,i}$ and no last-column variables, projects by the Fischer Gram matrix to the $\sigma$ Weyl space, and multiplies by $$\prod_\tau c_{\lambda_\tau,\sigma_\tau}\frac{\langle\xi_{\lambda_\tau,\sigma_\tau},\xi_{\lambda_\tau,\sigma_\tau}\rangle_F}{\langle v_{\lambda_\tau},v_{\lambda_\tau}\rangle_F},$$ where $v_\lambda$ is the extremal polynomial. Let $M'_\tau\subset K^n$ be any $\mathcal O_K$-submodules and $t_\tau\in K^\times$, and put $$r_t=\left(\prod_\tau t_\tau^{-b_\tau}\right)r_0.$$ For a tuple of submodules $M_\tau$, define $\Delta_\lambda((M_\tau))$ by requiring that, at every finite prime and in every local basis for $M_\tau$, inverse change of basis puts the polynomial in the localized tensor product of the standard integral Weyl lattices. Then $$r_t\bigl(\Delta_\lambda((M'_\tau\oplus\mathcal O_Kt_\tau)_\tau)\bigr)\subseteq\Delta_\sigma((M'_\tau)_\tau).$$
