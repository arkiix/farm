import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "flags",
    component: () => import("@/views/Flags.vue"),
  },
  {
    path: "/teams",
    name: "teams",
    component: () => import("@/views/Teams.vue"),
  },
  {
    path: "/login",
    name: "login",
    component: () => import("@/views/Login.vue"),
  },
  {
    path: "/charts",
    name: "charts",
    component: () => import("@/views/Charts.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
