---
{
  "module": "src/Formalism/LocalToGlobal/ProjectiveLattices/ThGerm.lean",
  "declarations": [
    "Formalism.L2.Pj.ChartAt",
    "Formalism.L2.Pj.IsNab"
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

## Canonical derivative charts for theta sections

[Definition / hypothesis ARAK.D217](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.IsNab/)

Use the universal polarized abelian scheme, its $\mathcal O_E$-action, symmetric rigidified line bundle $\mathcal L$, chosen cubical trivialization, and framed points from ([Polarized modules and unitary moduli](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Host/)) and ([Flag models and logarithmic Kodaira–Spencer maps](https://andrewodesky.com/rh/lean/GlobalTheory.CompHS.TorFlag/)). The involution on $\mathcal O_E$ is required to be the specified CM conjugation. Fix the chosen host element $w_0=(1+\rho)/2\in\mathcal O_E$, where $\rho$ is its designated square root of $-d$. A derivative operation assigns a scalar $\nabla_y(k,s,\alpha)$ to a framed point $y$ over a coefficient algebra $R$, a section $s$ of $\mathcal L^k$ on its fibre, a natural $k$, and a multiindex $\alpha$ on the finite set of frame labels.

Hypothesis (canonical derivative charts). For every commutative coefficient algebra $R$ which is also a $\mathbb Q$-algebra, and every such framed point $y$, the following choices and conditions hold.

Choose a natural $d$, a $d$-variable formal addition law $F(x,y)$ over $R$, and formal endomorphisms $A_a(x)$ for $a\in\mathcal O_E$. Every component has zero constant coefficient. Require $$F(0,x)=x,\quad F(x,y)=F(y,x),\quad F(F(x,y),z)=F(x,F(y,z)),$$ $$A_a(F(x,y))=F(A_ax,A_ay),\quad A_{a+b}(x)=F(A_ax,A_bx),\quad A_{ab}(x)=A_a(A_bx),\quad A_1(x)=x.$$ In the remaining formulas write $x\oplus y=F(x,y)$ and $ax=A_a(x)$; these are formal substitutions.

Choose scalar formal power series $\phi_1(x,y,z),\phi_2(x,y,z),\sigma(x,y)$ and $a_a(x,y)$ for each $a\in\mathcal O_E$. Each of $\phi_1,\phi_2$ is $1$ if any argument is zero; $\sigma$ and every $a_a$ are $1$ if either argument is zero. Require the following identities: $$\phi_1(x,y,w)\phi_1(x\oplus y,z,w)=\phi_1(y,z,w)\phi_1(x,y\oplus z,w),\qquad \phi_1(y,x,z)=\phi_1(x,y,z),$$ $$\phi_2(x,y,z)\phi_2(x,y\oplus z,w)=\phi_2(x,z,w)\phi_2(x,y,z\oplus w),\qquad \phi_2(x,z,y)=\phi_2(x,y,z),$$ $$\phi_1(x,y,z)\phi_1(x,y,w)\phi_2(x\oplus y,z,w)=\phi_2(x,z,w)\phi_2(y,z,w)\phi_1(x,y,z\oplus w),$$ $$\sigma(x,y)\sigma(y,x)=1,$$ $$\phi_2(x,y,z)\sigma(x,y)\sigma(x,z)=\sigma(x,y\oplus z)\phi_1(y,z,x),$$ $$\phi_1(ax,ay,z)a_a(x\oplus y,z)=a_a(x,z)a_a(y,z)\phi_1(x,y,\bar a z),$$ $$\phi_2(ax,y,z)a_a(x,y\oplus z)=a_a(x,y)a_a(x,z)\phi_2(x,\bar a y,\bar a z),$$ $$a_1(x,y)=1,\qquad a_{ab}(x,y)=a_a(bx,y)a_b(x,\bar a y),$$ $$\phi_1(ax,bx,y)a_{a+b}(x,y)=a_a(x,y)a_b(x,y)\phi_2(x,\bar a y,\bar b y),$$ $$a_a(x,y)a_{\bar a}(y,x)\sigma(ax,y)=\sigma(x,\bar a y).$$ Here the bar in $\bar a$ is CM conjugation; the formal series $a_a$ is distinct from the action $A_a$.

For every $m\ge0$, put $J_m^{(n)}=R[z_{b,j}:0\le b<n,\ 0\le j<d]/(z)^{m+1}$. Choose a point $x_m$ of the universal abelian scheme over $J_m^{(1)}$, above $y$, which reduces to zero at $z=0$ and is compatible under all truncations. Applying $x_m$ to the constant-free truncation of $F$ gives the sum of its two independent copies over $J_m^{(2)}$; applying it to the constant-free truncation of $A_a$ gives the action of $a$ on $x_m$. For each frame label $\ell$ choose $u_\ell\in R^d$. Its linear combination of the tangent vectors of $x_1$ is the designated tangent-frame vector at $\ell$. The vectors $u_\ell$ are a basis in the literal sense that every $v\in R^d$ has a unique expression $v=\sum_\ell b_\ell u_\ell$.

Write $$\mathcal E(x,y)=\mathcal L_{x+y}\otimes\mathcal L_x^{-1}\otimes\mathcal L_y^{-1}\otimes\mathcal L_0.$$ For every jet order choose an everywhere-generating frame $e_m(x,y)$ of $\mathcal E$ at the two copies of $x_m$. The chosen cubical trivialization $c$ has, after the indicated jet substitutions, the two expressions $$c(x,y,z)=\phi_1(x,y,z)\frac{e_m(x\oplus y,z)}{e_m(x,z)e_m(y,z)},\qquad c(y,z,x)=\phi_2(x,y,z)\frac{e_m(x,y\oplus z)}{e_m(x,y)e_m(x,z)}.$$ These equations mean equality under the canonical tensor identifications of the displayed line bundles. The truncations of the multiplying series are required to be units. Symmetry requires $e_m(y,x)=\sigma(x,y)e_m(x,y)$. For every $a\in\mathcal O_E$ there is a global generating frame $w_a$ of $\mathcal E(x,\bar a y)\otimes\mathcal E(ax,y)^{-1}$ such that, at every jet order, $$w_a(x,y)e_m(ax,y)=a_a(x,y)e_m(x,\bar a y).$$

Choose a global generating frame $w_P$ of $\mathcal L_x\otimes\mathcal E(x,w_0x)^{-1}$. Its restriction at zero agrees with the given rigidification of $\mathcal L$. Let $$e_{\mathcal L,m}(x)=w_P(x)e_m(x,w_0x).$$ At order zero this frame also agrees with the rigidification after the augmentation $J_0^{(1)}\to R$.

Choose $h(x,y)\in R[[x,y]]$ with $h(0,y)=h(x,0)=0$, satisfying $$\phi_1(x,y,z)=\exp\{h(x,z)+h(y,z)-h(x\oplus y,z)\},$$ $$\phi_2(x,y,z)=\exp\{h(x,y)+h(x,z)-h(x,y\oplus z)\},$$ $$\sigma(x,y)=\exp\{h(y,x)-h(x,y)\},\qquad a_a(x,y)=\exp\{h(ax,y)-h(x,\bar a y)\}.$$ The exponentials are formal exponentials over the $\mathbb Q$-algebra $R$.

Every section $s$ of every $\mathcal L^k$, including $k=0$, has a formal germ $f(x)$ in these charts: at every order, pull back $s$ to the jet, choose the frame corresponding to $e_{\mathcal L,m}^k$, and its coefficient is the truncation of $f$. For any formal germ with these equalities, define the invariant derivation $$D_u f(x)=\sum_j\left(\sum_i u_i\frac{\partial F_j}{\partial y_i}(x,0)\right)\frac{\partial f}{\partial x_j}(x).$$ Compose $D_{u_\ell}^{\alpha_\ell}$ in the fixed enumeration of the frame labels, and call the resulting operator $D^\alpha$. Require $$\nabla_y(k,s,\alpha)=\left[D^\alpha\left(f(x)\exp\{k h(x,w_0x)\}\right)\right]_{x=0}.$$ Thus the identity is required for every section and every formal germ realizing it, with the same chosen chart and scalar series at $y$.
