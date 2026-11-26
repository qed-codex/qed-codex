---
{
  "module": "src/Formalism/SharpRestriction/Divisibility/BoundaryLocalData.lean",
  "declarations": [
    "Formalism.MainNotions.BoundaryLocalData.LocB"
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

## Boundary characters and integral Fourier jets

[Definition / hypothesis PHT.D158](https://andrewodesky.com/rh/lean/Formalism.MainNotions.BoundaryLocalData.LocB/)

Hypothesis (boundary characters and integral Fourier jets). Use ([Integral charts and theta representations](https://andrewodesky.com/rh/lean/Formalism.MainNotions.ModuliIntegralCharts.CF/)), for a prime $p$, with its notation, and set $w_0=(1+\sqrt{-d})/2\in\mathcal O_E$. For a unit $u$ in any of the valued fields $C_y$, put $v_p(u)=-\log_p|u|$. For each $y\in P_Z$, choose an $\mathcal O_E$-module $X_y$, an additive isomorphism $\varphi_y:\Lambda_y\to X_y$ with $\varphi_y(\bar c a)=c\varphi_y(a)$, and a pairing $t_y:\Lambda_y\times X_y\to C_y^\times$. Require $$t(a+a',\chi)=t(a,\chi)t(a',\chi),\quad t(a,\chi+\chi')=t(a,\chi)t(a,\chi'),$$ $$t(a,\varphi b)=t(b,\varphi a),\quad t(ca,\chi)=t(a,c\chi),\quad\beta_y(a,b)=v_p(t_y(a,\varphi_y b)).$$ Choose two arbitrary maps $m_1,m_2:\Lambda_y\times\Lambda_y\to X_y$ and a map $m:\Lambda_y\times\Lambda_y\to C_y^\times$, requiring $\psi_y(a)=v_p(m_y(a,w_0a))$.

For $U\in\mathcal U$, choose sets $\mathcal A_U,\mathcal Q_U$, a map $r_2:\mathcal A_U\to\mathcal Q_U$, an element $q_U\in\mathcal Q_U$, a predicate on $\mathcal A_U$, and maps $d:\mathcal A_U\to\mathcal B_U$, $d_{\mathbb Q}:\mathcal Q_U\to\mathcal B_U^{\mathbb Q}$, satisfying $$q(d(a))=d_{\mathbb Q}(r_2(a)),\qquad P_U=d_{\mathbb Q}(q_U).$$ These sets and their predicate are specified labels; no additional henselian or acyclicity condition is imposed by this hypothesis.

Choose a set $B$. For $b\in B$, choose a complete Noetherian integrally closed local domain $R_b$, with completeness for its maximal ideal, and put $F_b=\operatorname{Frac}R_b$. Choose $\mathcal O_E$-modules $Y_b,X_b$, an additive isomorphism $\varphi_b:Y_b\to X_b$ with $\varphi_b(\bar c a)=c\varphi_b(a)$, and a pairing $t_b:Y_b\times X_b\to F_b^\times$ satisfying both additivity-to-multiplicativity identities, symmetry through $\varphi_b$, and $t_b(ca,\chi)=t_b(a,c\chi)$. Require $t_b(a,\varphi_ba)$ to belong to the image of $R_b$ in $F_b$. Choose an $F_b$-vector space $S_b$, an $R_b$-module structure compatible with restriction of scalars, an $R_b$-submodule $S_b^0$, an $F_b$-linear map $$\operatorname{fc}_b:S_b\to\{X_b\to F_b\},$$ and an arbitrary map $Y_b\times X_b\to R_b^\times$.

Choose an invariant object $\mathcal O\in\mathcal S_{X_m}$ and maps $\operatorname{Iso}(\mathcal O,A)\to S(A)$, $\phi\mapsto s_\phi$, for every $A\in\mathcal S_{X_m}$, with $\lVert s_\phi\rVert_y=p^{-v_\phi(y)}$. If $L_{\rm pp}$ is invariant, every distinguished $L_c$ must be invariant. Choose integers $b_y\ge0$ for $y\in P_{X_m}$ satisfying $b_y+\operatorname{rank}_{\mathbb Z}\Lambda_y=fr$.

For each $y\in P_{X_m}$, $a,n\ge0$ and tuple $\chi\in X_y^a$, choose a $C_y$-vector space $F_{y,a,n,\chi}$, a real function $N_B$ on this space, and a linear map $$\operatorname{sg}_\chi:V_{y,U_a,n}\to F_{y,a,n,\chi}.$$ For $t\in\Lambda_y^a$, choose linear isomorphisms $$T_t:F_{y,a,n,\chi}\xrightarrow\sim F_{y,a,n,\chi+n\varphi_y(t)}$$ preserving $N_B$.

Call $n$ permitted when it is odd, coprime to $p$, and either a square or the norm $\pi\bar\pi$ of an integral $\pi\in E$ lying in the fixed quadratic subfield. Choose $\alpha_n\in\mathcal O_E$ for all $n$. For permitted $n$, require $$\alpha_n\bar\alpha_n=n,\qquad (\exists m\ge0:\ n=m^2,\ \alpha_n=m)\ \text{or}\ \alpha_n\in E_0,$$ where $E_0$ is that quadratic subfield. Choose $\vartheta_{y,a}^{(1)}\in V_{y,U_a,1}$ and linear maps $P_n:V_{y,U_a,1}\to V_{y,U_a,n}$; for permitted $n$, the distinguished vector of ([Integral charts and theta representations](https://andrewodesky.com/rh/lean/Formalism.MainNotions.ModuliIntegralCharts.CF/)) must be $P_n\vartheta_{y,a}^{(1)}$.

For every $y,a,n,D,\chi$, choose a linear map $$J_\chi:F_{y,a,n,\chi}\to J_{y,U_a,n,D}.$$ The integral additive subgroup of $J_{y,U_a,n,D}$ has a finite $C_y$-basis in which membership is exactly the condition that all coordinates have norm at most one. Require $N_B(s)\le1\Rightarrow J_\chi(s)\in J^0_{y,U_a,n,D}$. For every $s\in V_{y,U_a,n}$ and every nonzero $t\in C_y$, there is a finite set $F_0\subseteq X_y^a$ such that, for every finite $F\supseteq F_0$, $$\operatorname{jet}(s)-\sum_{\chi\in F}J_\chi(\operatorname{sg}_\chi s)\in tJ^0_{y,U_a,n,D}.$$
