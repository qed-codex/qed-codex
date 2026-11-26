---
{
  "module": "src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/RowsDef.lean",
  "declarations": [
    "Formalism.L2.SG.RowsDef.RowsFinDim"
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

## Hypothesis: the range of a product of a finite-adelic and a discrete-series convolution operator on a unitary group is finite-dimensional

[Definition / hypothesis THETA.D258](https://andrewodesky.com/rh/lean/Formalism.L2.SG.RowsDef.RowsFinDim/)

The hypothesis concerns square-integrable functions on an adelic unitary group modulo its rational points. It asserts that two convolution operators, one on the finite adelic part and one built from matrix coefficients of irreducible unitary representations at the infinite places, have a product of finite rank.

**Setting.** Let $E'/F'$ be a CM extension of number fields in the sense of ([Hermitian spaces in the theta constructions](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.CMData/)), $n\ge0$ an integer, $J\in M_n(E')$ a nonsingular Hermitian matrix, and $L\subset(E')^n$ a full, finitely generated $\mathcal O_{E'}$-lattice that is self-dual for the form $\sum_{i,j}\bar x_iJ_{ij}y_j$. For every infinite place $v$ of $F'$ let $\phi_v:E'\hookrightarrow\mathbb C$ be an embedding above $v$, $\epsilon_v$ a list of $n$ signs with diagonal matrix $J_{\epsilon_v}$, and $P_v\in\mathrm{GL}_n(\mathbb C)$ a matrix with $P_v^*\phi_v(J)P_v=J_{\epsilon_v}$. Let $$G_\infty=\prod_vU(J_{\epsilon_v}),\qquad U(J_{\epsilon_v})=\{g\in M_n(\mathbb C):\ g^*J_{\epsilon_v}g=J_{\epsilon_v}\},$$ let $G_f$ be the unitary group of $J$ over the finite adeles of $F'$, with a group topology in which the subgroups $\{x:\ x\widehat L=\widehat L,\ (x-1)\widehat L\subseteq N\widehat L\}$, $N\ge1$, are open and form a basis of neighbourhoods of $1$, and let $G_A=G_\infty\times G_f$. These are the choices of the first paragraph of Hypothesis (spectral unitary setting) of ([Spectral column and period realizations](https://andrewodesky.com/rh/lean/Formalism.L2.SG.HidaSetting.HidaSetting/)). The group $\Gamma$ of matrices $\gamma\in\mathrm{GL}_n(E')$ preserving $J$ is embedded in $G_A$ by $\gamma\mapsto\bigl((P_v^{-1}\phi_v(\gamma)P_v)_v,\gamma\bigr)$.

Each $U(J_{\epsilon_v})$ carries a fixed Haar measure $\mu_v$; put $\mu_\infty=\prod_v\mu_v$.

**Hypothesis.** In every such setting, make the following further choices.

1. A $\sigma$-finite Haar measure $\mu_f$ on $G_f$; put $\mu_A=\mu_\infty\times\mu_f$.
2. A measurable set $\mathcal F\subset G_A$ such that every $y\in G_A$ has a translate $\gamma y\in\mathcal F$ with $\gamma\in\Gamma$, and $\mu_A(\gamma\mathcal F\cap\mathcal F)=0$ for every $\gamma\in\Gamma$ with $\gamma\ne1$. Put $\mathscr H=L^2(\mathcal F,\mu_A)$. For $f\in\mathscr H$ let $\widetilde f$ be the function on $G_A$ with $\widetilde f(y)=f(\gamma_yy)$, where for each $y$ an element $\gamma_y\in\Gamma$ with $\gamma_yy\in\mathcal F$ has been chosen.
3. Continuous linear operators $R(g)$ on $\mathscr H$, $g\in G_A$, with $(R(g)f)(x)=\widetilde f(xg)$ for almost every $x\in\mathcal F$.
4. A locally constant function $e:G_f\to\mathbb C$ that vanishes outside the stabilizer of $\widehat L$ and is integrable for $\mu_f$, and a continuous linear operator $R_e$ on $\mathscr H$ with $$\langle x,R_ey\rangle=\int_{G_f}e(g)\,\langle x,R(1,g)y\rangle\,d\mu_f(g)\qquad(x,y\in\mathscr H).$$
5. For every infinite place $v$: a complex Hilbert space $H_v$, a map $\sigma_v$ from $M_n(\mathbb C)$ to the continuous linear operators on $H_v$, a real number $d_v$ and a vector $w_v\in H_v$ with $\|w_v\|=1$, such that - $\sigma_v(1)=1$, $\sigma_v(gh)=\sigma_v(g)\sigma_v(h)$ and $\|\sigma_v(g)\xi\|=\|\xi\|$ for $g,h\in U(J_{\epsilon_v})$ and $\xi\in H_v$, and $g\mapsto\sigma_v(g)\xi$ is continuous on $U(J_{\epsilon_v})$ for every $\xi$; - the only closed subspaces of $H_v$ stable under all $\sigma_v(g)$, $g\in U(J_{\epsilon_v})$, are $0$ and $H_v$; - $d_v>0$, and for all $\xi,\eta,\xi',\eta'\in H_v$ the function $g\mapsto\langle\eta,\sigma_v(g)\xi\rangle\,\overline{\langle\eta',\sigma_v(g)\xi'\rangle}$ is integrable on $U(J_{\epsilon_v})$ with $$\int_{U(J_{\epsilon_v})}\langle\eta,\sigma_v(g)\xi\rangle\,\overline{\langle\eta',\sigma_v(g)\xi'\rangle}\,d\mu_v(g)=\frac{\langle\xi',\xi\rangle\,\langle\eta,\eta'\rangle}{d_v};$$ - the function $g\mapsto d_v\,\overline{\langle w_v,\sigma_v(g)w_v\rangle}$ is integrable on $U(J_{\epsilon_v})$.
6. A continuous linear operator $T$ on $\mathscr H$ with $$\langle x,Ty\rangle=\int_{G_\infty}\varphi(g)\,\langle x,R(g,1)y\rangle\,d\mu_\infty(g)\quad(x,y\in\mathscr H),\qquad\varphi(g)=\Bigl(\prod_vd_v\Bigr)\overline{\prod_v\langle w_v,\sigma_v(g_v)w_v\rangle}.$$

Then the range of $R_eT$ is a finite-dimensional subspace of $\mathscr H$.
