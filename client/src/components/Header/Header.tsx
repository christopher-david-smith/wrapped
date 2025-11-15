import React from "react";
import { Group, Title, Button, Burger, Drawer, Stack, useMantineTheme } from "@mantine/core";
import { useDisclosure, useMediaQuery } from "@mantine/hooks";

interface PageLink<T extends string = string> {
  key: T;
  name: string;
};

interface HeaderProps<T extends string = string> {
  title?: React.ReactNode;
  pages: PageLink<T>[];
  activeTab: T;
  onSwitchTab: (key: T) => void;
};

export const Header = <T extends string = string>({
  title = "wrapped",
  pages,
  activeTab,
  onSwitchTab
}: HeaderProps) => {

  const theme = useMantineTheme();
  const isDesktop = useMediaQuery(`(min-width: ${theme.breakpoints.sm})`);
  const [opened, { close, toggle }] = useDisclosure(false);

  const buttons = (
    <>
      {pages.map((page) => {
        return (
          <Button
            key={page.key}
            variant={activeTab === page.key ? "filled" : "light"}
            onClick={() => {
              onSwitchTab(page.key); if (!isDesktop) close();
            }}
          >
            {page.name}
          </Button>
        )
      })}
    </>
  );

  return (
    <Group justify="space-between" px="md" h="100%">
      <Title>{title}</Title>

      {!isDesktop ? (
        <>
          <Burger opened={opened} onClick={toggle} />
          <Drawer opened={opened} onClose={close} size="100%">
            <Stack gap="sm">
              {buttons}
            </Stack>
          </Drawer>
        </>
      ) : (
        <Group>
          {buttons}
        </Group>
      )}

    </Group>
  );
};
