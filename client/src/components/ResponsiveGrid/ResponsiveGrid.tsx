import React from "react";

interface ResponseiveGridProps {
  children: React.ReactNode;
  className?: string;
  minWidth?: number;
  gap?: number;
}

export const ResponseiveGrid = ({
  children,
  className,
  minWidth = 200,
  gap = 20
}: ResponseiveGridProps) => {
  return (
    <div
      className={className}
      style={{
        display: "grid",
        gridTemplateColumns: `repeat(auto-fill, minmax(${minWidth}px, 1fr))`,
        gap: `${gap}px`
      }}
    >
      {React.Children.map(children, (child) => (
        <div>{child}</div>
      ))}
    </div>
  );
};
