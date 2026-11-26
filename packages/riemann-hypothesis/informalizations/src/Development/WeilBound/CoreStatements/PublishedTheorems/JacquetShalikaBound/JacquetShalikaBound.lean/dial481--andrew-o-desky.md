---
{
  "module": "src/Development/WeilBound/CoreStatements/PublishedTheorems/JacquetShalikaBound/JacquetShalikaBound.lean",
  "declarations": [
    "PositivityTheory.JacquetShalikaLocal.jacquetShalikaBound",
    "PositivityTheory.JacquetShalikaLocal.l4b",
    "PositivityTheory.JacquetShalikaLocal.l5",
    "PositivityTheory.JacquetShalikaLocal.l7",
    "PositivityTheory.JacquetShalikaLocal.l9"
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

## Bounds for unramified Satake eigenvalues

[Theorem REP.1116](https://andrewodesky.com/rh/lean/PositivityTheory.JacquetShalikaLocal.jacquetShalikaBound/)

Let $E$ be a totally complex number field and $\pi$ a unitary cuspidal automorphic representation of $\mathrm{GL}_a(\mathbb A_E)$. If $\pi$ has the unramified Satake multiset $B_w$ at a finite place $w$, with $q_w$ the residue-field cardinality, then every $\alpha\in B_w$ satisfies $$q_w^{-1/2}<|\alpha|<q_w^{1/2}.$$

## Positivity of a stabilized Whittaker column average

[Theorem REP.1509](https://andrewodesky.com/rh/lean/PositivityTheory.JacquetShalikaLocal.l4b/)

Let $F$ be a nonarchimedean local field with valuation ring $\mathcal O$ and uniformizer $\varpi$, and let $\mu$ be an additive Haar measure for its Borel structure. Let $\psi:F\to\mathbb C^\times$ be unitary, trivial on $\mathcal O$ and nontrivial on $\varpi^{-1}\mathcal O$. Let $\rho$ be a smooth complex representation of $\mathrm{GL}_n(F)$ on $V$, $\lambda:V\to\mathbb C$ a Whittaker functional for $\psi$, and $k\ge0$ with $k+1<n$.

Index matrices by $0,\ldots,n-1$. Write $U_m$ for the upper unitriangular matrices whose columns through $m$ equal those of the identity, and $P_m$ for matrices whose rows from $m$ onward and columns strictly after $m$ equal those of the identity. Put $\psi_N(u)=\psi(\sum_i u_{i,i+1})$ and let $c_k(x)$ be the identity with entries $x_0,\ldots,x_k$ inserted in column $k+1$ above the diagonal.

Let $B,B'$ be sesquilinear forms, conjugate-linear in their first argument. Assume $B$ is Hermitian and positive semidefinite, $B(v,v)=0$ implies $\lambda(v)=0$, and $$B(\rho(g)v,\rho(g)w)=|\det g|_F^{n-2-k}B(v,w)\quad(g\in P_{k+1}),$$ $$B(v,\rho(u)w)=\psi_N(u)B(v,w)\quad(u\in U_{k+1}).$$ Suppose that for each $v,w$ and all sufficiently large integers $M$, $$B'(v,w)=\int_{\varpi^{-M}\mathcal O^{k+1}}\psi(-x_k)B(v,\rho(c_k(x))w)\,d\mu^{k+1}(x).$$ Then $B'$ is Hermitian and positive semidefinite, and $B'(v,v)=0$ implies $\lambda(v)=0$.

## Bounded weighted partial sums for a stable character average

[Theorem REP.1527](https://andrewodesky.com/rh/lean/PositivityTheory.JacquetShalikaLocal.l5/)

Let $F$ be a nonarchimedean local field with residue cardinality $q$, uniformizer $\varpi$, additive Haar measure $\mu$, and an additive character $\psi:F\to\mathbb C$ of absolute value $1$, trivial on $\mathcal O_F$ but nontrivial on $\varpi^{-1}\mathcal O_F$. Let $n>1$, let $\rho$ be a smooth complex representation of $\operatorname{GL}_n(F)$, and let $l:V\to\mathbb C$ be linear. Let $B,B'$ be conjugate-linear in the first variable and linear in the second. For zero-based matrix indices, put $$P_1=\{g:g_{ij}=\delta_{ij}\text{ if }i\ge1\text{ or }j>1\},$$ and let $U_1$ be the upper unitriangular subgroup whose first two columns are standard. Write $\psi_N(u)=\psi(\sum_{i=0}^{n-2}u_{i,i+1})$. Assume $B$ is Hermitian, $\operatorname{Re}B(u,u)\ge0$, and $B(u,u)=0$ implies $l(u)=0$. Assume also $$B(\rho(g)u,\rho(g)u')=|\det g|^{n-2}B(u,u')\quad(g\in P_1),$$ $$B(u',\rho(g)u)=\psi_N(g)B(u',u)\quad(g\in U_1).$$ For every $u,u'$, suppose that for all sufficiently large integers $M$, $$B'(u',u)=\int_{\varpi^{-M}\mathcal O_F}\psi(-x)B(u',\rho(1+xE_{0,1})u)\,d\mu(x).$$ For every $v\in V$ fixed by $\operatorname{GL}_n(\mathcal O_F)$, there is $C\in\mathbb R$ such that for every integer $T\ge0$, $$\sum_{j=0}^{T-1}q^{j(n-2)}\operatorname{Re}B'(\rho(a_j)v,\rho(a_j)v)\le C,\qquad a_j=\operatorname{diag}(\varpi^j,1,\ldots,1).$$

## The Whittaker function of a spherical Hecke eigenvector

[Theorem REP.1596](https://andrewodesky.com/rh/lean/PositivityTheory.JacquetShalikaLocal.l7/)

Let $F$ be a nonarchimedean local field, with ring of integers $O$, uniformizer $\varpi$, and residue cardinality $q$. Let $\psi:F\to\mathbb C^\times$ be a unitary additive character trivial on $O$ and nontrivial on $\varpi^{-1}O$. Fix $n\ge0$, a complex representation $\rho$ of $\operatorname{GL}_n(F)$, and $z_1,\ldots,z_n\in\mathbb C^\times$. Let $v$ be fixed by $K=\operatorname{GL}_n(O)$ and satisfy $$T_rv=q^{r(n-r)/2}e_r(z_1,\ldots,z_n)v\quad(0\le r\le n),$$ where $T_r$ is the sum over right $K$-cosets in $K\operatorname{diag}(\varpi I_r,I_{n-r})K$ and $e_r$ is the elementary symmetric polynomial. If $l$ is a complex-linear functional with $l(\rho(u)x)=\psi(\sum_{i=1}^{n-1}u_{i,i+1})l(x)$ for upper unitriangular $u$, then $$l(\rho(g)v)=l(v)W_z(g).$$ For an Iwasawa decomposition $g=u\operatorname{diag}(\varpi^{\lambda_1},\ldots,\varpi^{\lambda_n})k$, $k\in K$, the function on the right is $$W_z(g)=\begin{cases}\psi(\sum_i u_{i,i+1})\delta_B^{1/2}(\operatorname{diag}(\varpi^\lambda))s_\lambda(z),&\lambda_1\ge\cdots\ge\lambda_n,\\0,&\text{otherwise},\end{cases}$$ where $\delta_B$ is the modulus character of the upper Borel and $s_\lambda$ is the Schur Laurent polynomial.

## Decay of a recurrence forces its parameters into the unit disc

[Theorem ALG.1613](https://andrewodesky.com/rh/lean/PositivityTheory.JacquetShalikaLocal.l9/)

Let $n\ge0$, let $\beta_1,\ldots,\beta_n\in\mathbb C$, and let $g:\mathbb N\to\mathbb C$. Put $$e_r(\beta)=\sum_{\substack{S\subseteq\{1,\ldots,n\}\\|S|=r}}\prod_{i\in S}\beta_i,$$ with $e_0=1$ and $e_r=0$ for $r>n$. Assume $g(0)=1$ and $$\sum_{r=0}^{j}(-1)^r e_r(\beta)g(j-r)=0\qquad(j\ge1).$$ If $g(j)\to0$ as $j\to\infty$, then $|\beta_i|<1$ for every $i$.
