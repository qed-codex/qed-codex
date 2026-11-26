---
{
  "module": "src/Formalism/LocalToGlobal/BesselHermitianTheta/TiedWeilEq.lean",
  "declarations": [
    "Formalism.L2.Theta.TwRuleEq",
    "Formalism.L2.Theta.WeilCompatibleEquivariance"
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

## Adelic oscillator actions and theta integrals

[Definition / hypothesis ARAK.D153](https://andrewodesky.com/rh/lean/Formalism.L2.Theta.WeilTied/)

Use ([Automorphic theta functions and their measures](https://andrewodesky.com/rh/lean/Formalism.L2.Theta.ThetaTied/)) and ([Hermitian theta spaces and pairings](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.ThetaX/)). Put $A_E=\mathbb A_F\otimes_F E$ and write $\bar x$ for CM conjugation, $G_V=U(V)(\mathbb A_F)$ and $G_V(F)=U(V)(F)$. Identify each Hermitian space with its prescribed coordinate basis and write $G_V^0$ for its rational Gram matrix. For spaces $V,W$ of ranks $v,w$, put $Z_{V,W}=\operatorname{Mat}_{v,w}(A_E)$. Define $$H_{V,W}(x,y)=\begin{cases}\sum_{i,j,k,l}\bar x_{ij}(G_V^0)_{ki}(G_W^0)_{jl}y_{kl},&v\le w,\\\sum_{i,j,k,l}\bar x_{ij}(G_V^0)_{ik}(G_W^0)_{lj}y_{kl},&v>w,\end{cases}$$ $$[x,y]=\operatorname{Tr}_{A_E/\mathbb A_F}(\xi_0H_{V,W}(y,x)),\qquad (g,h)\cdot x=\begin{cases}\bar gxh^t,&v\le w,\\gx\bar h^t,&v>w.\end{cases}$$ Here $\xi_0=-1/(N\mathfrak c\,s_d)$ uses the ideal and square root in ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)), and group elements in matrix formulas mean their coordinate matrices. Choose an additive character $\psi:\mathbb A_F\to\mathbb C$ that is continuous, has modulus one, is nontrivial and is trivial on $F$. At infinity, for every compatible embedding family in ([Automorphic theta functions and their measures](https://andrewodesky.com/rh/lean/Formalism.L2.Theta.ThetaTied/)), require $$\psi_\infty(x)=\exp\left(-2\pi i\sum_\tau\theta_\tau(x\otimes1)\right).$$ Set $T_u f(x)=\psi([x,u]/2)f(x+u)$. A theta function on $Z_{V,W}$ means a continuous function satisfying $$f(\gamma+x)=\psi(-[\gamma,x]/2)f(x)\quad(\gamma\in\operatorname{Mat}_{v,w}(E)),$$ fixed under $T_u$ for every purely finite $u$ in some open additive subgroup of $Z_{V,W}$, and smooth along every continuous additive map $\mathbb R^d\to Z_{V,W}$ with zero finite part, at every translated base point.

Hypothesis (adelic oscillator realization). Choose injective complex-linear maps $e_{V,W}:\mathcal S(V,W)\to\{Z_{V,W}\to\mathbb C\}$ and, for every pair of abstract characters $\chi,\chi'$, a representation $\omega_{\chi,\chi'}$ of $G_V\times G_W$ on $\mathcal S(V,W)$. For $v\ne w$ the image of $e_{V,W}$ is exactly the theta functions. Let the restriction conditions on $\chi,\chi'$ mean that their corresponding Hecke characters restrict on $\mathbb A_F^\times$ to the $v$th and $w$th powers of every quadratic norm character in ([Automorphic theta functions and their measures](https://andrewodesky.com/rh/lean/Formalism.L2.Theta.ThetaTied/)). For $v\ne w$ and all character pairs satisfying these conditions, require the following laws.

For every $g,h,u,\Phi,\Phi'$ with $e\Phi'=T_u(e\Phi)$, $$e(\omega_{\chi,\chi'}(g,h)\Phi')=T_{(g,h)\cdot u}\bigl(e(\omega_{\chi,\chi'}(g,h)\Phi)\bigr).$$ For rational $\gamma\in G_V(F)$ and $\gamma'\in G_W(F)$, evaluation of $e(\omega(\gamma,\gamma')\Phi)$ at zero equals $e\Phi(0)$. For every $\Phi,x$, its value $e(\omega(g,h)\Phi)(x)$ is continuous in $(g,h)$. For every additive Haar measure $\nu$ on $Z_{V,W}$ and every fundamental domain $\mathcal F$ for its rational matrix subgroup, $$\int_{\mathcal F}|e(\omega(g,h)\Phi)(x)|^2d\nu(x)=\int_{\mathcal F}|e\Phi(x)|^2d\nu(x).$$ These are real Bochner integrals with the total convention zero for a nonintegrable function.

A split idempotent is an $e\in A_E$ with $e^2=e$, $e\bar e=0$ and $e+\bar e$ the idempotent supported at one finite $F$-place. Suppose $g,h$ are supported there, meaning $(e+\bar e)(g-1)=g-1$ and similarly for $h$. Put $x=e\det g+1-e$ and $y=e\det h+1-e$ and require these elements to be units. There is a real $r>0$, common to all functionals $\ell$ below, such that $$\ell(\omega_{\chi,\chi'}(g,h)\Phi)=r\,c_{\chi,\chi'}(x,y)\ell(\Phi).$$ This holds for every complex-linear $\ell$ invariant under all realized $T_u$ with $\bar e u=u$, and every $\Phi$. Here the characters on units are their Hecke realizations and $$c_{\chi,\chi'}(x,y)=\begin{cases}\chi'(x)^{-1}\chi(y),&v\le w,\\\chi'(x)\chi(y)^{-1},&v>w.\end{cases}$$ An idele $a$ is a determinant root for $g$ when $a=\det(g)\bar a$. For every character $\nu$ with trivial restriction to $\mathbb A_F^\times$, twisting $\chi'$ by $\nu$ multiplies $\omega(g,h)$ by $\nu(a)^{-1}$ if $v<w$ and by $\nu(a)$ if $v>w$, for every determinant root $a$ of $g$. Twisting $\chi$ by $\nu$ multiplies it by $\nu(b)$ if $v<w$ and by $\nu(b)^{-1}$ if $v>w$, for every determinant root $b$ of $h$.

If $e_{W,V}\Phi'(x^t)=e_{V,W}\Phi(x)$ for all $x$, require $$e_{W,V}(\omega_{\chi',\chi}(h,g)\Phi')(x^t)=e_{V,W}(\omega_{\chi,\chi'}(g,h)\Phi)(x).$$ When $V$ has correct Gram signatures, for every compatible measure and rational fundamental domain from ([Automorphic theta functions and their measures](https://andrewodesky.com/rh/lean/Formalism.L2.Theta.ThetaTied/)) and every cuspidal $F$, $$e_W\bigl(\Theta_{V,W}^{\chi,\chi'}(\Phi,F)\bigr)(h)=p(V)\int_{\mathcal F_V}e_{V,W}(\omega_{\chi,\chi'}(g,h)\Phi)(0)\,e_VF(g)\,d\nu_V(g).$$

Hypothesis (equal-rank oscillator laws). For $v=w$, require the same image characterization, Heisenberg covariance, rational evaluation, continuity, integral norm equality, split-functional law and theta integral just stated, with the same restriction conditions. Require twisting $\chi'$ by a trivial-restriction $\nu$ to multiply the action by $\nu(a)^{-1}$, and twisting $\chi$ to multiply it by $\nu(b)$, for every determinant root of $g$ and $h$, respectively. The transpose law above is imposed only in the unequal-rank hypothesis.

Hypothesis (unramified vectors). Suppose $v\ne w$, the character restrictions hold and $S$ is a finite set of $F$-places. Require $\chi,\chi'$ to be trivial on finite integral units whose components at $S$ are one and whose infinite part is one. Let $\Lambda_S(V,W)$ be the additive subgroup generated by tensors $$\alpha\otimes\bigl(a\bar x_i y_j\bigr)_{ij}\ (v\le w),\qquad \alpha\otimes\bigl(ax_i\bar y_j\bigr)_{ij}\ (v>w),$$ where $\alpha\in\widehat{\mathcal O}_F$ vanishes at $S$, $a$ lies in the fractional ideal $\mathfrak A=(\mathfrak c\mathcal O_E)\mathfrak b_0^{-1}$, using the chosen ideals of ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)), and $x\in L_V$, $y\in L_W$. If $e\Phi$ is fixed by every $T_u$ with $u\in\Lambda_S(V,W)$, then $\omega(k,k')\Phi=\Phi$ for all finite adelic $k,k'$ preserving the respective completed lattices and equal to one at $S$.

Finally require, for every twist $\mu$ and $j<m$, $$e_{Y_j,Y_{j+1}}(\Phi^+_{\mu,j})(x^t)=e_{Y_{j+1},Y_j}(\Phi_{\mu,j})(x).$$
