---
{
  "module": "src/Formalism/SharpRestriction/GlobalSchurBounds/GL3Columns.lean",
  "declarations": [
    "Formalism.MainNotions.GL3Columns.KFTie",
    "Formalism.MainNotions.GL3Columns.KFTie.UnIs"
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

## Finite-kernel basis comparisons

[Definition / hypothesis PHT.D185](https://andrewodesky.com/rh/lean/Formalism.MainNotions.GL3Columns.KFTie/)

Hypothesis (finite-kernel basis comparison). Use ([Rational kernel entries and derivative minors](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.KerEnt/)) and ([Geometric theta-lift data](https://andrewodesky.com/rh/lean/Formalism.MainNotions.GL3Theta.LiftObj/)) for the same twisted chain, and fix a coefficient prime $w$. For each stage, class and embedding choose a matrix $B_{i,c,\tau}\in M_{N_i}(\mathbb C_{p_w})$. For $i\le m$ require it to be invertible and satisfy both conditions: every vector of $L_{i,c}$, embedded through $\lambda_w e_\tau$, has coordinates of absolute value at most one in this basis; and every column of $B_{i,c,\tau}$ is a finite linear combination of embedded vectors of $L_{i,c}$ with coefficients of absolute value at most one.

Choose $c_{i,c,c',\tau}\in\mathbb C_{p_w}$ of absolute value one for all natural $i$ and adjacent class pairs. For $i<m$ the formal series of ([Rational kernel entries and derivative minors](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.KerEnt/)) is exactly the Taylor series of the complex $\Theta_{i,c,c'}$, with coefficients mapped through $\lambda_w$, after the linear substitution $$X_{\tau,b,a}\longmapsto\sum_{\substack{z,a',b'\\\tau_z=\tau}}c_{i,c,c',\tau}\lambda_w(c^D_\tau)(B_{i+1,c',\tau})_{b,b'}(B_{i,c,\tau}^{-1})_{a',a}Z_{z,a',b'}.$$ Taylor coefficients mean $\partial^\alpha\Theta(0)/\alpha!$; coefficients outside $\overline{\mathbb Q}$ are mapped to zero by the convention of ([Rational kernel entries and derivative minors](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.KerEnt/)).

For matrix tuples $Y_\tau\in M_n(\mathbb C_{p_w})$ set $$\Delta_n(Y;X)=\prod_{z,\text{ columns of }\mathcal Y_{z,i}}\det\left(\sum_{a<n}X_{z,r,a}(Y_{\tau_z})_{a,s}\right)_{r,s<h}.$$ For every $i<m$, $c$ and $v\in V_{i,c}$ there is a polynomial $Q\in\overline{\mathbb Q}[X_{\tau,a,b}:a,b<N_i]$ such that $$\operatorname{sharp}_i(e(v))(y)=Q(f_i(y)),$$ $$S^w(v)(\Delta_{N_i}(Y;X))=\left(\prod_\tau\det(B_{i,c,\tau})^{-s^{\rm sharp}_{i,\tau}}\right)\lambda_w(Q)((B_{i,c,\tau}Y_\tau)_\tau)$$ for every matrix tuple $Y$. All indices $z,\mathcal Y_{z,i}$ and minor polynomials have the meaning in ([Rational kernel entries and derivative minors](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.KerEnt/)); the $z$ in this minor product is its signed embedding label, not the source label.

For every $i<m$, target class $c'$ and $v'\in V_{i+1,c'}$, there are a polynomial $Q'\in\overline{\mathbb Q}[X_{\tau,a,b}:a,b<N_{i+1}]$ and a linear functional $\phi$ on the target minor-polynomial ring such that $$\left(\prod_\tau d_{i+1}(y',\tau)^{s^{\rm div}_{i,\tau}}\right)e(v')(y')=Q'(f_{i+1}(y')),$$ $$T^w(v')(I)=\phi(\nabla_{N_{i+1},I}),\qquad\phi(\Delta_{N_{i+1}}(Y';X))=\left(\prod_\tau\det(B_{i+1,c',\tau})^{-s^{\rm div}_{i,\tau}}\right)\lambda_w(Q')((B_{i+1,c',\tau}Y'_\tau)_\tau)$$ for every $I,Y'$. Complex polynomial evaluations in these identities use the inclusion $\overline{\mathbb Q}\subset\mathbb C$.

Define $$u_S(i,c)=\lambda_w(r_i(t_{i,c}))\prod_\tau\det(B_{i,c,\tau})^{s^{\rm sharp}_{i,\tau}},\quad u_T(i,c')=\lambda_w(r'_i(t_{i+1,c'}))\prod_\tau\det(B_{i+1,c',\tau})^{-s^{\rm div}_{i,\tau}},$$ $$c_K(i,c,c')=\left(\prod_z c_{i,c,c',\tau_z}^{|\mathcal Y_{z,i}|}\right)^{-1},\qquad u(i,c,c')=c_K(i,c,c')u_S(i,c)u_T(i,c').$$ The scalar comparison law means $u^w_{i,c,c'}=u(i,c,c')$ for every $i<m,c,c'$. It is an additional condition on this basis comparison.
