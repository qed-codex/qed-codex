---
{
  "module": "src/Formalism/AdmissibleDesigns/RestrictedSevenEightOfFull.lean",
  "declarations": [
    "Formalism.MainNotions.N.K.Rows.AllDesignConditions"
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

## Congruence objects of a system of Galois representations at an eigensystem

[Definition / hypothesis GC.D275](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.GoodCongruenceObjects/)

Congruence objects are the algebraic data with which the congruences between an eigensystem $\pi$ and the other eigensystems at a local coefficient index are studied. They consist of two orthogonal idempotents $e_B$, of rank $t$, and $e_1$, of rank one, in the span of the family $R=(R_x)$; an element $X_0=e_BX_0e_B$ of that span which, at $\pi$, acts as an inertia element $\sigma_0$ above $\ell$ on the sum of the $t$ characters $\xi_{i,c}$ and as zero on $\varrho_\pi$; a finite cover $X'$ of the set of eigensystems on which the $t$ roots of the characteristic polynomial of $X_0$ on the image of $e_B$ are functions $\rho_1,\dots,\rho_t$; and maps that read the diagonal blocks of the family at the point $\pi'$ of the cover above $\pi$. From them one forms an element $E$ which has rank one at every point of the cover and which, at $\pi'$, is a multiple of the projection onto the line on which $G_E$ acts through $\xi_{i,1}$.

**Setting.** The setting and notation are those of ([Systems of Galois representations over the eigensystems at a local coefficient index: conditions, Selmer group and local terms](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TruncatedSeriesCountingIdentities.admitted/)): a local coefficient index $i$ with $\ell=\ell_i$, and a system $(R,\varrho,\pi,\mathcal P',\mathcal P'',\lambda,e',c_B)$ at $i$. Only $R$, $\varrho$ and $\pi$ enter the definition. Put $n=n_V$.

For a finite set $Y$, the ring $\mathrm M_n(O_i)^Y$ of functions $Y\to\mathrm M_n(O_i)$ has pointwise operations, and it is a module over $O_i^Y$ by $(fa)(y)=f(y)a(y)$. For $g\in G_E$ let $R(g)\in\mathrm M_n(O_i)^{X_i}$ be the function $x\mapsto R_x(g)$, and let $\mathcal R\subseteq\mathrm M_n(O_i)^{X_i}$ be the $\mathbb T_i$-submodule spanned by the elements $R(g)$, $g\in G_E$. For a map $p:X'\to X_i$ of finite sets and a subalgebra $\mathbb T'\subseteq O_i^{X'}$, let $R'(g)\in\mathrm M_n(O_i)^{X'}$ be the function $x'\mapsto R_{p(x')}(g)$, and let $\mathcal R'$ be the $\mathbb T'$-submodule of $\mathrm M_n(O_i)^{X'}$ spanned by the elements $R'(g)$, $g\in G_E$.

**Definition.** *Congruence objects* for $(R,\varrho,\pi)$ consist of

- (i) elements $e_B$, $e_1$ and $X_0$ of $\mathrm M_n(O_i)^{X_i}$;
- (ii) an element $\sigma_0\in G_E$;
- (iii) a finite set $X'$ with a map $p:X'\to X_i$ and a point $\pi'\in X'$, an $O_i$-subalgebra $\mathbb T'\subseteq O_i^{X'}$, and functions $\rho_1,\dots,\rho_t:X'\to O_i$;
- (iv) a $K_i$-linear isomorphism $\theta:K_i^{n}\to K_i^{r}\times K_i^{t}$;
- (v) maps $\psi:\mathcal R'\to\mathrm M_r(O_i)$ and $\psi_c:\mathcal R'\to O_i$ for $1\le c\le t$;

with the following eleven properties. We say that $\theta$ *carries* a matrix $A\in\mathrm M_n(K_i)$ to $A_1\times A_2$, with $A_1\in\mathrm M_r(K_i)$ and $A_2\in\mathrm M_t(K_i)$, if $\theta(Au)=(A_1u_1,A_2u_2)$ whenever $\theta(u)=(u_1,u_2)$.

1. *Idempotents.* $e_B,e_1\in\mathcal R$; $e_B^2=e_B$, $e_1^2=e_1$ and $e_Be_1=e_1e_B=0$; and for every $x\in X_i$ the matrix $e_B(x)$ has rank $t$ and the matrix $e_1(x)$ has rank $1$ over $K_i$.
2. *The decomposition at $\pi$.* For every $g\in G_E$, $\theta$ carries $R_\pi(g)$ to $\varrho_\pi(g)\times\operatorname{diag}\bigl(\xi_{i,1}(g),\dots,\xi_{i,t}(g)\bigr)$.
3. *The blocks at $\pi'$.* For every $a\in\mathcal R'$, $\theta$ carries $a(\pi')$ to $\psi(a)\times\operatorname{diag}\bigl(\psi_1(a),\dots,\psi_t(a)\bigr)$.
4. *Surjectivity.* The map $\psi:\mathcal R'\to\mathrm M_r(O_i)$ is surjective.
5. *The element $\sigma_0$.* There is a place $w$ of $E$ above $\ell$ with $\sigma_0\in I_w$, and the image of $\sigma_0$ under the cyclotomic character $G_E\to\mathbb Z_\ell^\times$ is $1+\ell^{u_i}u$ with $u\in\mathbb Z_\ell^\times$.
6. *The corner.* $X_0\in\mathcal R$, $e_BX_0=X_0e_B=X_0$, and $\theta$ carries $X_0(\pi)$ to $0\times\operatorname{diag}\bigl(\xi_{i,1}(\sigma_0),\dots,\xi_{i,t}(\sigma_0)\bigr)$.
7. *The cover.* $\mathbb T'$ contains $f\circ p$ for every $f\in\mathbb T_i$ and contains $\rho_1,\dots,\rho_t$, and it is generated as an $O_i$-algebra by these elements. There are $b_1,\dots,b_{t!}\in\mathbb T'$ such that every element of $\mathbb T'$ can be written in exactly one way as $\sum_{k=1}^{t!}(f_k\circ p)\,b_k$ with $f_k\in\mathbb T_i$. Every fibre of $p$ has $t!$ elements.
8. *Eigenvalues of the corner.* For every $x'\in X'$, with $x=p(x')$, $$\prod_{c=1}^{t}\bigl(X-\rho_c(x')\bigr)=\det\bigl(X\,e_B(x)-X_0(x)+1-e_B(x)\bigr)\quad\text{in }O_i[X].$$
9. *The point $\pi'$.* $p(\pi')=\pi$, and $\rho_c(\pi')=\xi_{i,c}(\sigma_0)$ for $1\le c\le t$.
10. *The element of rank one.* For $x'\in X'$ with $x=p(x')$ put $$E(x')=\prod_{c=2}^{t}\bigl(X_0(x)-\rho_c(x')\,e_B(x)\bigr)\in\mathrm M_n(O_i),\qquad\delta(x')=\prod_{c=2}^{t}\bigl(\rho_1(x')-\rho_c(x')\bigr)\in O_i.$$ Then, for every $x'\in X'$, the matrix $E(x')$ has rank $1$ over $K_i$ and $E(x')^2=\delta(x')E(x')$; $\theta$ carries $E(\pi')$ to $0\times\operatorname{diag}\bigl(\delta(\pi'),0,\dots,0\bigr)$; and $$\operatorname{len}_\ell\bigl(O_i/\delta(\pi')O_i\bigr)=\Delta_i.$$
11. *Determinants.* (a) For every $m\ge0$, all $a_1,\dots,a_m\in\mathcal R'$ and every monomial in the variables $Y_1,\dots,Y_m$, the function that sends $x'\in X'$ to the coefficient of that monomial in $\det\bigl(\sum_{k=1}^mY_k\,a_k(x')\bigr)\in O_i[Y_1,\dots,Y_m]$ belongs to $\mathbb T'$. (b) For every $q\ge0$ and every family $(\Theta_{jk})_{1\le j,k\le q}$ of elements of $\mathcal R'$, the function that sends $x'\in X'$ to the determinant of the $qn\times qn$ matrix with blocks $\Theta_{jk}(x')$ belongs to $\mathbb T'$.

**Hypothesis (existence of congruence objects).** For every local coefficient index $i$ with $\ell_i\notin\{g_0,g_1\}$ and every system $(R,\varrho,\pi,\mathcal P',\mathcal P'',\lambda,e',c_B)$ at $i$ that satisfies the conditions of ([Systems of Galois representations over the eigensystems at a local coefficient index: conditions, Selmer group and local terms](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TruncatedSeriesCountingIdentities.admitted/)) and has $\pi\in Z_i$, there are congruence objects for $(R,\varrho,\pi)$.
