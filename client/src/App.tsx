import "@mantine/core/styles.css";
import { useState } from "react";
import { AppShell } from "@mantine/core";
import { IdeasPage, PeoplePage, ChristmasPage } from "./pages";
import { Header } from "./components/Header/Header";

export default function App() {

  const pages = [
    { key: "ideas", name: "Ideas", component: <IdeasPage /> },
    { key: "people", name: "People", component: <PeoplePage /> },
    { key: "christmas", name: "Christmas", component: <ChristmasPage /> },
  ];

  const [activeTab, setActiveTab] = useState<string>("ideas");
  const currentPage = pages.find((page) => page.key === activeTab);

  return (
    <AppShell
      padding="md"
      header={{ height: 60 }}
    >

      <AppShell.Header>
        <Header
          title="wrapped"
          pages={pages}
          activeTab={activeTab}
          onSwitchTab={setActiveTab} />
      </AppShell.Header>

      <AppShell.Main>
        {currentPage?.component && currentPage.component}
      </AppShell.Main>

    </AppShell >
  );
}
