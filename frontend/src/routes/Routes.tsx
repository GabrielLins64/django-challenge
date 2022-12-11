import { Suspense } from "react";
import {
  // Navigate,
  Route,
  Routes as RoutesReactRouterDom,
} from "react-router-dom";
import LoadingPage from "../pages/LoadingPage/LoadingPage";
import { Example } from "./paths";

export function Routes() {
  return (
    <Suspense fallback={<LoadingPage />}>
      <RoutesReactRouterDom>
        <Route path="/" element={<Example />} />
      </RoutesReactRouterDom>
    </Suspense>
  );
}
