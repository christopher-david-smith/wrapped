import { IconLink, IconTrash } from "@tabler/icons-react";
import { Card, Text, Group, ActionIcon } from "@mantine/core";
import styles from "./Gifts.module.scss"
import { API } from "../../api/client";

export interface GiftProps {
  id: number;
  createdAt: string;
  name: string;
  labels?: string[];
  ideaHandedOutCount?: number;
  onDelete: (id: number) => void | Promise<void>;
}

export const Gift = (props: GiftProps) => {
  const handedOut: boolean = (props.ideaHandedOutCount ?? 0) > 0;
  return (
    <Card
      shadow="sm"
      padding="lg"
      radius="md"
      withBorder
    >
      <Text fw={700} size="lg">
        {props.name}
      </Text>
      <Group gap="xs" mt="lg">
        <ActionIcon
          component="a"
          variant="filled"
          color="red"
          onClick={() => props.onDelete(props.id)}
        >
          <IconTrash />
        </ActionIcon>
      </Group>
    </Card >
  )
}
