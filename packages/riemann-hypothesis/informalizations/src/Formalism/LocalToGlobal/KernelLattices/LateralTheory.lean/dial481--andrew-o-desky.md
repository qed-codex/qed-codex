---
{
  "module": "src/Formalism/LocalToGlobal/KernelLattices/LateralTheory.lean",
  "declarations": [
    "Formalism.L2.Ker.Base",
    "Formalism.L2.Ker.IsoKG",
    "Formalism.L2.Ker.KapChoice"
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

## Standard period bases for kernel theta functions

[Definition / hypothesis THETA.D180](https://andrewodesky.com/rh/lean/Formalism.L2.Ker.IsoKG/)

Hypothesis (standard kernel period basis). Use ([Ideal characters and period lattices](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TaylorLogMetric.Tor/)) and ([Fourfold theta kernels and lattice intertwiners](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.H.StdData/)). Choose a period pair $P$ whose additive period lattice is $\Lambda=\delta\varphi_0(\mathfrak c)$, and a complex number $\omega_0$ such that, with $t_0=\omega_0/2$, $$2t_0\in\Lambda,\qquad\frac{1+\mathrm i\sqrt d}{2}t_0\notin\Lambda,\qquad\frac{1-\mathrm i\sqrt d}{2}t_0\notin\Lambda.$$ Choose an $E_0$-linear isomorphism $\gamma_0:E^4\simeq E_0^{\{0,1,2,3\}\times\mathcal T}$ satisfying $$\sum_w\gamma_0(x)_w\overline{\gamma_0(y)_w}=\sum_{a=0}^3\operatorname{Tr}_{E/E_0}(x_a\bar y_a),$$ with both sides viewed in $E$. Also choose a complex-linear automorphism $g$ of $\mathbb C^{\{0,1,2,3\}\times\mathcal T}$ such that $$g((e_\tau(x_a))_{a,\tau})=(\varphi_0(\gamma_0(x)_{a,\tau}))_{a,\tau}\qquad(x\in E^4).$$

Call a rational prime $p$ selected if $p=2$ or $\left(\frac{-d}{p}\right)=1$, with the Jacobi-symbol convention for the latter expression. For every natural number $p$, choose a nonzero prime ideal $\mathfrak p_p\subset\mathcal O_{E_0}$, an element $\pi_p\in\mathcal O_{E_0}$, a trace isometry $\gamma_p$ of the same kind as $\gamma_0$, and $r_p\in\mathbb C$. For selected prime $p$, require $$p\in\mathfrak p_p,\qquad\mathfrak p_p^{h_0}=\pi_p\mathcal O_{E_0},\qquad r_p^{2h_0}=\frac{\varphi_0(\pi_p)}{\varphi_0(\bar\pi_p)},\qquad h_0=h(E_0).$$ Require also that $\gamma_p$ and its inverse are integral at $p$ in the following precise sense: if all four coordinates of $x$ lie in $A_0$, there is a natural integer $s$ coprime to $p$ for which every coordinate of $s\gamma_p(x)$ is integral; if every coordinate of $v$ is integral, some natural $s$ coprime to $p$ has every coordinate of $s\gamma_p^{-1}(v)$ in $A_0$. The coprimality condition itself forces $s>0$ for prime $p$.

Put $$y_p=\operatorname{ord}_{\mathfrak p_p}\det(\gamma_p\gamma_0^{-1}),\qquad\kappa=\prod_{p\text{ selected prime}}r_p^{-y_p},\qquad\Lambda_M=\langle(w e_\tau(a))_\tau:w\in\Lambda,\ a\in A_0\rangle_{\rm add}.$$ The valuation convention is $\operatorname{ord}_{\mathfrak p}(0)=0$. The product is the total finite product: it is one if infinitely many factors differ from one. No finite-support assertion is included here.

Let $H_0(z,w)=\operatorname{area}(P)^{-1}\sum_\tau z_\tau\bar w_\tau$ and $c=\sqrt d/2$. Fix a function $\theta_M:\mathbb C^{\mathcal T}\to\mathbb C$ as follows. If a function exists in the theta space $\mathcal T(H_0,\alpha_c^{H_0},\Lambda_M)$ whose fourfold tensor power equals $\kappa$ times the fourfold kernel attached to $(P,\omega_0,\Lambda_M,g)$ with $\beta(x)=\exp(\pi\mathrm i c\operatorname{area}(P)^{-1}\sum_{a,\tau}|x_{a,\tau}|^2)$ in ([Fourfold theta kernels and lattice intertwiners](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.H.StdData/)), choose such a function; otherwise use the fixed arbitrary value of this choice operation.

For each $N,N'$ put $\theta_0(z)=\prod_{i<N'}\prod_{j<N}\theta_M((z_{\tau ij})_\tau)$. Let $L_N^0=\mathcal O_E^N$. Using the normalized lattice changes $I$ of ([Ideal characters and period lattices](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TaylorLogMetric.Tor/)), define $$\theta_{L,L'}=I_{\mathcal L(L,L^0_{N'}),\mathcal L(L,L')}\,I_{\mathcal L(L_N^0,L^0_{N'}),\mathcal L(L,L^0_{N'})}\theta_0,$$ $$\gamma^{\rm nat}_{N,N',L,L'}=\chi([L_N^0:L]_{\det})^{\lfloor N'/2\rfloor}\chi([L^0_{N'}:L']_{\det})^{-\lfloor N/2\rfloor},\qquad e^{\rm nat}_{N,N',L,L'}=\gamma^{\rm nat}_{N,N',L,L'}\theta_{L,L'}.$$ These formulas define the chosen family of functions; they do not add existence, holomorphy, norm, integrality or nonvanishing assertions about it.
