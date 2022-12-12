import { Suspense } from "react";
import {
  Navigate,
  Route,
  Routes as RoutesReactRouterDom,
} from "react-router-dom";
import LoadingPage from "../pages/LoadingPage/LoadingPage";
import { Home, Login, NotFound } from "./paths";

export function Routes() {
  return (
    <Suspense fallback={<LoadingPage />}>
      <RoutesReactRouterDom>
        <Route path="/" element={<Navigate to="/login" />} />
        <Route path="/login" element={<Login />} />
        <Route path="/home" element={<Home />} />
        <Route path="*" element={<Navigate to="/notfound" />} />
        <Route path="/notfound" element={<NotFound />} />
      </RoutesReactRouterDom>
    </Suspense>
  );
}
