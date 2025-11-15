import ReactDOM from "react-dom/client";
import { MantineProvider } from "@mantine/core";
import App from "./App.tsx";

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <MantineProvider defaultColorScheme="auto">
    <App />
  </MantineProvider>
);
