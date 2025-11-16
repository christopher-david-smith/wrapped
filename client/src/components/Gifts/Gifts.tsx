import { IconLink, IconTrash } from "@tabler/icons-react";
import { Card, Text, Group, Image, ActionIcon } from "@mantine/core";
import styles from "./Gifts.module.scss"
import { API } from "../../api/client";

export interface GiftProps {
  id: number;
  createdAt: string;
  name: string;
  url?: string;
  image?: string;
  labels?: string[];
  ideaHandedOutCount?: number;
  onDelete: (id: number) => void | Promise<void>;
}

const PLACEHOLDER = 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="400" height="240"><rect width="100%" height="100%" fill="%23eee"/><text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="sans-serif" font-size="16" fill="%23999">No image</text></svg>';

export const Gift = (props: GiftProps) => {
  const handedOut: boolean = (props.ideaHandedOutCount ?? 0) > 0;
  return (
    <Card
      shadow="sm"
      padding="lg"
      radius="md"
      withBorder
    >
      <Card.Section>
        <Image
          className={handedOut ? styles.dim : undefined}
          src={PLACEHOLDER}
          height={160}
          fit="cover"
          fallbackSrc={PLACEHOLDER} />
      </Card.Section>
      <Group justify="space-between" mt="md" mb="xs">
        <Text fw={700} size="lg">
          {props.name}
        </Text>
        <Group gap="xs">
          <ActionIcon variant="filled"><IconLink /></ActionIcon>
          <ActionIcon
            component="a"
            variant="filled"
            color="red"
            onClick={() => props.onDelete(props.id)}
          >
            <IconTrash />
          </ActionIcon>
        </Group>
      </Group>
    </Card >
  )
}
